#  Extract URLs from a String: Develop a Python script to extract all URLs from a given 
# string, assuming URLs start with http:// or https:// and end with a space or 
# punctuation.
#q50
import re

text = input("Enter the text to find URLs: ")
reg = r'https?://\S+'

urls = re.findall(reg, text)

if urls:
    print("URLs found:")
    for url in urls:
        print(url)
else:
    print("No URLs found.")


# The regular expression r'https?://\S+?(?=[.,;:\s]|$)' 
# matches URLs that start with http:// or https://, followed 
# by non-whitespace characters, and stops before encountering 
# punctuation or whitespace or at the end of the string.

