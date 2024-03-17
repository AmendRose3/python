a=[1,67,98,54,23,78,9,88]
max=0
index=0
i=0
while i<len(a)-1:
    if a[i]>a[i+1]:
        max=a[i]
        index=i
    i+=1

if a[index]<a[-1]:
    max=a[-1]
    index=len(a) - 1


print(f'Maximum number is {max}')
print(f'at index {index+1}')