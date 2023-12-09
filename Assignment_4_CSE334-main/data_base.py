"""Calculate student grades by combining data from many sources.

Using Pandas, this script combines data from the:

* Roster
* Homework & Exam grades
* Quiz grades

to calculate final grades for a class.
"""
#Importing Libraries and Setting Paths
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import re
HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

#Data Importation and Cleaning
roster = pd.read_csv(DATA_FOLDER / "roster.csv")
hw_exam_grades = pd.read_csv(DATA_FOLDER / "hw_exam_grades.csv")
hw_exam_grades_submission_cols = hw_exam_grades.filter(regex="Submission")
hw_exam_grades.drop(columns=hw_exam_grades_submission_cols, axis=1)


quiz_grades = pd.DataFrame()

#Your code here to read the quiz_grades
quiz1 = pd.read_csv(DATA_FOLDER / "quiz_1_grades.csv", index_col="Email")
quiz1.rename(columns={
    'Grade':'Quiz 1'
}, inplace=True)

quiz2 = pd.read_csv(DATA_FOLDER / "quiz_2_grades.csv", index_col="Email")
quiz2.rename(columns={
    'Grade':'Quiz 2'
}, inplace=True)

quiz3 = pd.read_csv(DATA_FOLDER / "quiz_3_grades.csv", index_col="Email")
quiz3.rename(columns={
    'Grade':'Quiz 3'
}, inplace=True)

quiz4 = pd.read_csv(DATA_FOLDER / "quiz_4_grades.csv", index_col="Email")
quiz4.rename(columns={
    'Grade':'Quiz 4'
}, inplace=True)

quiz5 = pd.read_csv(DATA_FOLDER / "quiz_5_grades.csv", index_col="Email")
quiz5.rename(columns={
    'Grade':'Quiz 5'
}, inplace=True)

quiz_grades = pd.concat([quiz1, quiz2, quiz3, quiz4, quiz5], axis=1)
quiz_grades = quiz_grades.T.drop_duplicates().T

#Data Merging: roaster and homework
roster["NetID"] = roster["NetID"].str.lower()
final_data = pd.merge(roster, hw_exam_grades, left_on='NetID', right_on='SID', how='outer')
final_data["Email Address"] = final_data["Email Address"].str.lower()

#Data Merging: Final data and quiz grades
quiz_grades = quiz_grades.drop(columns=["Last Name", "First Name"])
final_data = pd.merge(final_data, quiz_grades, left_on="Email Address", right_index=True, how='outer')
final_data = final_data.fillna(0)

#Data Processing and Score Calculation
n_exams = 3
#For each exam, calculate the score as a proportion of the maximum points possible.
#Remove pass once you have cerated written the for loop
final_data.set_index("NetID", inplace=True)
final_data = final_data.drop(columns=["ID", "Name"])
for n in range(1, n_exams + 1):
#Your Code here
    exam_column = "Exam " + str(n)
    exam_max_pts_column = exam_column + " - Max Points"
    result = final_data[exam_column] / final_data[exam_max_pts_column]
    final_data[f"Exam {n} Score"] = result

# Calculating Exam Scores:
# Filter homework and Homework - for max points
homework_scores =  final_data.filter(regex='^Homework \d+$')
homework_max_points = final_data.filter(regex='^Homework \d+ - Max Points$')

#Calculating Total Homework score
sum_of_hw_scores = homework_scores.sum(axis=1)
sum_of_hw_max = homework_max_points.sum(axis=1)
final_data["Total Homework"] = sum_of_hw_scores / sum_of_hw_max
print("Total Homework score")
print(final_data.head())

#Calculating Average Homework Scores
hw_max_renamed = homework_max_points.rename(columns=lambda x: x.split(" - ")[0])  # Rename columns for easier calculation
average_hw_scores = (homework_scores / hw_max_renamed).mean(axis=1)
final_data["Average Homework"] = average_hw_scores 
print("Average Homework score")
print(final_data.head())

#Final Homework Score Calculation
final_data["Homework Score"] = final_data[["Total Homework", "Average Homework"]].max(axis=1)
print("Final Homework score")
print(final_data.head())

#Calculating Total and Average Quiz Scores:
#Filter the data for Quiz scores
quiz_scores = final_data.filter(regex='^Quiz \d$')
quiz_max_points = pd.Series(
    {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12}
)

#Final Quiz Score Calculation:
sum_of_quiz_scores = quiz_scores.sum(axis=1)

sum_of_quiz_max = quiz_max_points.sum()
final_data["Total Quizzes"] = sum_of_quiz_scores / sum_of_quiz_max
print("Total Quizzes score")
print(final_data.head())

sum_quiz_scores = (quiz_scores / quiz_max_points).sum(axis=1)
print(sum_quiz_scores)
average_quiz_scores = sum_quiz_scores / 5
final_data["Average Quizzes"] = average_quiz_scores
print("Average Quizzes score")
print(final_data.head())

final_data["Quiz Score"] = sum_of_quiz_scores / sum_of_quiz_max
final_data["Quiz Score"] = final_data[["Quiz Score", "Average Quizzes"]].max(axis=1)
print("Final Quizzes score")
print(final_data.head())

#Calculating the Final Score:
weightings = pd.Series(
    {
        "Exam 1 Score": 0.05,
        "Exam 2 Score": 0.1,
        "Exam 3 Score": 0.15,
        "Quiz Score": 0.30,
        "Homework Score": 0.4,
    }
)
final_score = (final_data * weightings).sum(axis=1)
final_data["Final Score"] = final_score
print(final_data)
final_data.to_csv("final_data.csv", index=False)
#Rounding Up the Final Score:
final_data["Ceiling Score"] = (final_data["Final Score"]*100).apply(np.ceil).astype(float)
print("Rounding Up Final score")
print(final_data.head())

#Defining Grade Mapping:
grades = {
    90: "A",
    80: "B",
    70: "C",
    60: "D",
    0: "F",
}

#Applying Grade Mapping to Data:
def grade_mapping(value):
    for key, letter in grades.items():
        if (value >= key):
            return letter



letter_grades = final_data["Ceiling Score"].apply(grade_mapping)
final_data["Final Grade"] = letter_grades
#Processing Data by Sections:
for section, table in final_data.groupby("Section"):
    # print(section, table)
    file_to_save_to = DATA_FOLDER / f"Section {section} Grades.csv"
    table.to_csv(file_to_save_to)
    print(f"In Section {section} there are {len(table)} students saved to file")

#Visualizing Grade Distribution: Get Grade Counts and use plot to plot the grades
possible_grades = ['A', 'B', 'C', 'D', 'F']
grade_counts = final_data['Final Grade'].value_counts().reindex(possible_grades, fill_value=0)
grade_counts.name = 'Final Grade'
print(grade_counts)

plt.bar(grade_counts.index, grade_counts)
plt.show()

#Visualize the data on with Histogram and use Matplot lib density function to print Kernel Density Estimate
final_data["Final Score"].plot.hist(bins=20, label="Histogram")
final_data["Final Score"].plot.density(
    linewidth=4, label="Kernel Density Estimate",
)

#Plotting Normal Distribution:
final_mean = final_data["Final Score"].mean()
final_std = final_data["Final Score"].std()
print(final_mean)
print(final_std)

#Plot the normal distribution of final_mean and final_std
x = np.linspace(final_mean - 5 * final_std, final_mean + 5 * final_std, 1000)
pdf = scipy.stats.norm.pdf(x, final_mean, final_std)
plt.plot(x, pdf, color='green', label='Normal Distribution', linewidth=4) 
plt.legend(loc="upper right")
plt.show()
