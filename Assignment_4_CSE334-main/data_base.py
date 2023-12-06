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

HERE = Path(__file__).parent
DATA_FOLDER = HERE / "data"

#Data Importation and Cleaning
roster = pd.read_csv(DATA_FOLDER / "roster.csv")

hw_exam_grades = pd.read_csv(DATA_FOLDER / "hw_exam_grades.csv")
quiz_grades = pd.DataFrame()

#Your code here to read the quiz_grades
quiz1 = pd.read_csv(DATA_FOLDER / "quiz_1_grades.csv", index_col="Email")
quiz1.rename(columns={
    'Grade':'quiz_1_grades'
}, inplace=True)

quiz2 = pd.read_csv(DATA_FOLDER / "quiz_2_grades.csv", index_col="Email")
quiz2.rename(columns={
    'Grade':'quiz_2_grades'
}, inplace=True)

quiz3 = pd.read_csv(DATA_FOLDER / "quiz_3_grades.csv", index_col="Email")
quiz3.rename(columns={
    'Grade':'quiz_3_grades'
}, inplace=True)

quiz4 = pd.read_csv(DATA_FOLDER / "quiz_4_grades.csv", index_col="Email")
quiz4.rename(columns={
    'Grade':'quiz_4_grades'
}, inplace=True)

quiz5 = pd.read_csv(DATA_FOLDER / "quiz_5_grades.csv", index_col="Email")
quiz5.rename(columns={
    'Grade':'quiz_5_grades'
}, inplace=True)

quiz_grades = pd.concat([quiz1, quiz2, quiz3, quiz4, quiz5], axis=1)
quiz_grades = quiz_grades.T.drop_duplicates().T

#Data Merging: roaster and homework
roster["NetID"] = roster["NetID"].str.lower()
final_data = pd.merge(roster, hw_exam_grades, left_on='NetID', right_on='SID', how='outer')
final_data["Email Address"] = final_data["Email Address"].str.lower()

#Data Merging: Final data and quiz grades
final_data = pd.merge(final_data, quiz_grades, left_on="Email Address", right_index=True, how='outer')
final_data = final_data.fillna(0)

#Data Processing and Score Calculation
n_exams = 3
#For each exam, calculate the score as a proportion of the maximum points possible.
#Remove pass once you have cerated written the for loop
final_data.set_index("NetID", inplace=True)

final_data.to_csv("final_data.csv", index=False)
for n in range(1, n_exams + 1):
#Your Code here
    exam_column = "Exam " + str(n)
    exam_max_pts_column = exam_column + " - Max Points"
    result = final_data[exam_column] / final_data[exam_max_pts_column]
    final_data[f"Exam {n} Score"] = result
    # print(result)
print(final_data.head())
final_data.to_csv("final_data.csv", index=False)

# #Calculating Exam Scores:
# #Filter homework and Homework - for max points
# homework_scores = 
# homework_max_points = 

# #Calculating Total Homework score
# sum_of_hw_scores = 
# sum_of_hw_max = 
# final_data["Total Homework"] = 

# #Calculating Average Homework Scores
# hw_max_renamed = 
# average_hw_scores = 
# final_data["Average Homework"] = 

# #Final Homework Score Calculation
# final_data["Homework Score"] = 

# #Calculating Total and Average Quiz Scores:
# #Filter the data for Quiz scores
# quiz_scores = 

# quiz_max_points = pd.Series(
#     {"Quiz 1": 11, "Quiz 2": 15, "Quiz 3": 17, "Quiz 4": 14, "Quiz 5": 12}
# )

# #Final Quiz Score Calculation:
# sum_of_quiz_scores = 
# sum_of_quiz_max = 
# final_data["Total Quizzes"] = 

# average_quiz_scores = 
# final_data["Average Quizzes"] = 

# final_data["Quiz Score"] = 

# #Calculating the Final Score:
# weightings = pd.Series(
#     {
#         "Exam 1 Score": 0.05,
#         "Exam 2 Score": 0.1,
#         "Exam 3 Score": 0.15,
#         "Quiz Score": 0.30,
#         "Homework Score": 0.4,
#     }
# )

# final_data["Final Score"] = 

# #Rounding Up the Final Score:
# final_data["Ceiling Score"] = 

# #Defining Grade Mapping:
# grades = {
#     90: "A",
#     80: "B",
#     70: "C",
#     60: "D",
#     0: "F",
# }

# #Applying Grade Mapping to Data:
# def grade_mapping(value):
#    pass


# letter_grades = 
# final_data["Final Grade"] = 

# #Processing Data by Sections:
# for section, table in final_data.groupby("Section"):
#     pass

# #Visualizing Grade Distribution: Get Grade Counts and use plot to plot the grades
# grade_counts = 

# #Visualize the data on with Histogram and use Matplot lib density function to print Kernel Density Estimate
# final_data["Final Score"].plot.hist(bins=20, label="Histogram")
# final_data["Final Score"].plot.density(
#     linewidth=4, label="Kernel Density Estimate"
# )

# #Plotting Normal Distribution:
# final_mean = final_data["Final Score"].mean()
# final_std = final_data["Final Score"].std()

# #Plot the normal distribution of final_mean and final_std
