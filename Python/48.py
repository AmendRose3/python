# Extract Email Addresses Using Regex: Write a Python script that uses regular 
# expressions to extract all email addresses from a given text.
#q48
import re

text = input("Enter the text to find emails: ")
reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

x = re.findall(reg, text)
if x:
    print("Email addresses found:")
    for email in x:
        print(email)
else:
    print("No email addresses found.")

# \b: Match a word boundary.
# [A-Za-z0-9._%+-]+: Match one or more characters that can be letters (uppercase and lowercase),
    #  digits, or special characters like ._%+- before '@'.
# @: Match the '@' symbol.
# [A-Za-z0-9.-]+: Match one or more characters that can be letters 
    # (uppercase and lowercase), digits, or hyphen and dot after '@' but before the domain part.
# \.: Match a literal dot '.' in the domain part.
# [A-Z|a-z]{2,}: Match 2 or more uppercase or lowercase letters for the top-level domain (TLD) part.
# \b: Match another word boundary.