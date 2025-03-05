#-------------a function to extract all dates in the format MM-DD-YYYY from a given string----------

import re

def extract_dates(text):
    
    # Define the regular expression pattern for MM-DD-YYYY format
    pattern = r'\b\d{2}-\d{2}-\d{4}\b'
    
    # Use re.findall to find all matches of the pattern in the text
    dates = re.findall(pattern, text)
    
    return dates

# Input
text = "My birthday is on 12-10-1995 and my friend's birthday is 01-20-1990."
print(extract_dates(text))  