#-----------------a function to validate a password-------------------

import re

def validate_password(password):

    # Define the regular expression pattern for a strong password
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$'
    
    # Use re.match to check if the password matches the pattern
    if re.match(pattern, password):
        return True
    else:
        return False

# Input:
password1 = "Strong@123"
password2 = "weakpass"

print(validate_password(password1))  
print(validate_password(password2))