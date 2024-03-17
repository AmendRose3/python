# Display Students Scoring Above 85: Create a dictionary called 'students' where keys 
# are student names and values are their grades. The program should display all 
# students who scored more than 85.
#q38

record={'Amend':99,'stemin':100,'Athul':57}

def score():
    for key,value in record.items():
        if(value>85):
            print(f"Name:{key}")

def insertrecord():
    name=input("Enter name: ")
    mark=int(input("Enter mark: "))
    record[name]=mark

while(True):
    ch=int(input("enter choice 1:insert 2:show>85 3:exit"))
    if(ch==1):
        insertrecord()
    elif(ch==2):
        score()
    else:
        break
        
    

    
    

