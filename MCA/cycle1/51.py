#q51
import re
pass=input("enter the password")
reg='[0-9 A-B a-b]*[^0-9 A-B a-b]*'
x=re.search(reg,pass)
if x:
    print("VALID")
else:
    print("INVALID")
    
