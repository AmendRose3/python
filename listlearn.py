a=[1,2,3,4,5]
#2D list
b=[
    [11,12,13],
    [22,23,24]
]

for row in b:
    for item in row:
        print(item)

#methods in list
a.append(6)
print(a)
a.insert(0,0)
print(a)
