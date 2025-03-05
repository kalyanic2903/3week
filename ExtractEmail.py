#-----------------a function that extracts all email addresses from a given string-----------------


import re

def extract_emails(text):

    # Regular expression for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all function of the email pattern
    emails = re.findall(email_pattern, text)
    
    return emails

#Input:
text = "Contact john.doe@example.com, jane_doe123@domain.org for more details."
emails = extract_emails(text)
print(emails)