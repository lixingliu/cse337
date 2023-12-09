import re
from datetime import datetime


class PhysicalInfo:
    def __init__(self):
        self.date = None
        self.name = None
        self.gender = None
        self.height = None
        self.temperature = None

    def set_name(self, name_str):
        if not isinstance(name_str, str):
            raise ValueError("Name should be a string")

        # Define a regex pattern to match alphanumeric characters, spaces, or hyphens
        pattern = r'^[a-zA-Z0-9 -]+$'

        # Check if name_str matches the pattern using re.match()
        if not re.match(pattern, name_str):
            raise ValueError("Name should only contain alphanumeric, ' ', or '-' characters")

        # Count alphanumeric characters using regex, ensure at least 2 present
        alphanumeric_count = sum(1 for char in name_str if char.isalnum())

        if alphanumeric_count < 2:
            raise ValueError("Name should contain at least 2 alphanumeric characters")

        # Check if at least one alphabetical character is present
        if not any(char.isalpha() for char in name_str):
            raise ValueError("Name should contain at least one alphabetical character")

        self.name = name_str

    def set_gender(self, gender_str):
        if not isinstance(gender_str, str):
            raise ValueError("Gender should be a string")

        # Validate gender input - only accept 'M' or 'F'
        if gender_str not in ['M', 'F']:
            raise ValueError("Gender should be 'M' or 'F'")

        self.gender = gender_str


    def set_height(self, height_int):
        if not isinstance(height_int, int) or isinstance(height_int, bool):
            raise ValueError("Height should be a non-boolean integer")
        
        if height_int < 17 or height_int > 84:
            raise ValueError("Height should be between 17 and 84 (inclusive)")
        
        self.height = height_int

    def set_temperature(self, temperature_float):
        if not isinstance(temperature_float, float):
            raise ValueError("Temperature should be a float")

        # Check if the temperature is within the specified range [95.0, 104.0]
        if not (95.0 <= temperature_float <= 104.0):
            raise ValueError("Temperature should be between 95.0 and 104.0 (inclusive)")

        self.temperature = temperature_float
        
    def set_date(self, date_str):
        if not isinstance(date_str, str):
            raise ValueError("Date should be a string")
        # Validate date format (MM-DD-YYYY) and range (1900-2100)
        try:
            # Split the date string into components
            month, day, year = map(int, date_str.split('-'))
            date_obj = f"{month:02d}-{day:02d}-{year:04d}"
            if not (1 <= month <= 12) or not (1 <= day <= 31):
                raise ValueError("Month should be between 1-12 and day between 1-31")

            # Check if the date is a valid date in the range
            if not (1900 <= year <= 2100) or date_obj != date_str:
                raise ValueError("Date should be in MM-DD-YYYY format between 1900 and 2100")
        except (ValueError, IndexError):
            raise ValueError("Invalid date format. Please use MM-DD-YYYY format")

        self.date = date_str