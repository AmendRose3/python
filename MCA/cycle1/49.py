
#  Validate Date Format Using Regex: Implement a program that uses regular 
# expressions to verify if a given date string is in the format DD/MM/YYYY.
#q49
import re
dob = input("enter the date of birth")
reg=r'^(1[0-9]|0[1-9]|3[0-1])\/(1[0-2]|0[0-9])\/[1-9][0-9][0-9][1-9]$'
x=re.search(reg,dob)
if x:
    print("VALID")
else:
    print("INVALID")
    
