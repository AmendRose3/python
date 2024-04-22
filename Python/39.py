def set_operations(A, B):
    print("Set A:", A)
    print("Set B:", B)
    
    
    union_set = A.union(B)
    print("Union of A and B:", union_set)
    
    
    intersection_set = A.intersection(B)
    print("Intersection of A and B:", intersection_set)
    
   
    difference_AB = A.difference(B)
    print("Difference of A - B:", difference_AB)
    
    difference_BA = B.difference(A)
    print("Difference of B - A:", difference_BA)


A = set(input("Enter elements of set A separated by spaces: ").split())


B = set(input("Enter elements of set B separated by spaces: ").split())

set_operations(A, B)
