#------------a function to extract all hashtags (words starting with #) from a given string---------


import re

def extract_hashtags(text):

    # Define the regular expression pattern to match hashtags
    pattern = r'#\w+'
    
    # Use re.findall to find all matches of the pattern in the text
    hashtags = re.findall(pattern, text)
    
    return hashtags

# Input
text = "Loving the weather today! #sunny #goodvibes #relax"
print(extract_hashtags(text))  