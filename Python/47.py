def get_details(n):
    for _ in range(n):
        name = input("Enter name: ")
        height = int(input("Enter height: "))
        detail_tuple = (name, height)
        details_list.append(detail_tuple)
