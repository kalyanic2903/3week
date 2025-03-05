#----------- a function that replaces all consecutive whitespace characters (spaces, tabs, newlines) in a string with a single space--------


import re

def replace_whitespace(text):

    # Use regular expression \s+ to match one or more whitespace characters and replace them with a single space
    return re.sub(r'\s+', ' ', text).strip()

# Input:
text = "This    is    a   test  string.     "
print(replace_whitespace(text))  