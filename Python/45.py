details_list=[]

def get_details(n):
    for _ in range (n):
        detail_tuple=()
        name=input()
        height=int(input())
        detail_tuple=(name,height)
        details_list.append(detail_tuple)

def max_height():
    for i in range(len(details_list)):
        max_height=max(details_list[i][1],max_height)
    return max_height


n=int(input("enter number of people:"))
get_details(n)
max_height()


    
