#-----------------------a function to validate if a given URL is in the format http:// or https:// followed by a valid domain name and an optional path-------------------

import re

def valid_url(url):

    # Define the regular expression pattern for a valid URL
    pattern = r'^https?://[a-zA-Z0-9.-]+(?:/[a-zA-Z0-9/._-]*)?$'
    
    # Use re.match to check if the URL matches the pattern
    if re.match(pattern, url):
        return True
    else:
        return False

# Input:
print(valid_url("https://www.example.com/path/to/page"))  
print(valid_url("ftp://example.com"))  