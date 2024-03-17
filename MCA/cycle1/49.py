
#  Validate Date Format Using Regex: Implement a program that uses regular 
# expressions to verify if a given date string is in the format DD/MM/YYYY.
#q49
import re
dob = input("enter the date of birth")
reg=r'^\d{2}/\d{2}/\d{4}$'
x=re.search(reg,dob)
if x:
    print("VALID")
else:
    print("INVALID")
    
