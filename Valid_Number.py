#-----------------a function to check whether a given string is a valid phone number in the format (XXX) XXX-XXXX---------------------

import re

def valid_phone_number(phone):

    # Define the regular expression pattern
    pattern = r"^\(\d{3}\) \d{3}-\d{4}$"
    
    # Use re.match to check if the phone number matches the pattern
    if re.match(pattern, phone):
        return True
    else:
        return False

# Input:
print(valid_phone_number("(123) 456-7890"))  
print(valid_phone_number("123-456-7890")) 
