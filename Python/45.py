details_list = []

def get_details(n):
    for _ in range(n):
        name = input("Enter name: ")
        height = int(input("Enter height: "))
        detail_tuple = (name, height)
        details_list.append(detail_tuple)

def max_height():
    max_h = 0
    for i in range(len(details_list)):
        max_h = max(details_list[i][1], max_h)
    return max_h

n = int(input("Enter number of people: "))
get_details(n)
print("Maximum height is:", max_height())
