#-------------------a function that counts the number of words in a given string----------------------------


import re

def count_words(text):

    # Use regular expression \w+ to find words in the string
    words = re.findall(r'\w+', text)
    
    # Return the count of words found
    return len(words)

# Input:
text = "Hello, my name is John Doe."
print(count_words(text))  


