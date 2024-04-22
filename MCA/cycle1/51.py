#q51
# 51. Password Strength Checker Using Regex: Create a regular expression to check the 
# strength of a password. The password should have at least 8 characters, both 
# uppercase and lowercase letters, at least one digit, and at least one special character

import re
pass=input("enter the password")
reg='[0-9 A-B a-b]*[^0-9 A-B a-b]*'
x=re.search(reg,pass)
if x:
    print("VALID")
else:
    print("INVALID")
    
