# 52. Validate IPv4 Address Format: Write a program that validates whether a given string 
# is a valid IPv4 address, consisting of four numbers separated by dots, with each 
# number ranging from 0 to 255.
#q52
import re
add=input("enter the Address")
reg=ipv4_pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

x=re.search(reg,add)
if x:
    print("VALID")
else:
    print("INVALID")
    

