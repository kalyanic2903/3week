#--------------function to validate if a given string represents a valid date in the format DD-MM-YYYY----------

import re
from datetime import datetime

def validate_date(date_str):

    # Regular expression to check if the date matches the DD-MM-YYYY format
    pattern = r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}$"
    
    # Step 1: Check if the date matches the regex pattern
    if re.match(pattern, date_str):

        # Step 2: Use datetime to validate the actual date
        try:
            # Create a datetime object from the string
            datetime.strptime(date_str, "%d-%m-%Y")
            return True
        except ValueError:
            
            return False
    else:
        return False

# Input:
print(validate_date("15-04-2023"))  # True
print(validate_date("31-02-2023"))  # False
