# Count Unique Numbers in a List: Given a list L, create a dictionary where keys are 
# unique numbers from the list, and values are counts of those numbers. Display a set 
# of unique numbers from the list.
#q41
num=[]
record={}

def showrecord():
    for n in num:
        numc=num.count(n)
        if(n not in record):
            record[n]=numc

    print(record)

def insertrecord():
     n=int(input("Enter number: "))
     num.append(n)

while(True):
    ch=int(input("enter choice 1:insert 2:showrecord 3:exit"))
    if(ch==1):
        insertrecord()
    elif(ch==2):
        showrecord()
    else:
        break
