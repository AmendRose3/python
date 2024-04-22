#Q46
def countWords(s):
    l=s.split()
    print(l)
    d={}
    for i in l:
        if i not in d:
            c=1
            d[i]=c
        else:
            c=c+1
            d[i]=c

    unique=set()   #creating a set of unique words
    for i in list(d.keys()):
        if d[i]==1:   #if count of the particular word is 1, added to the set
            unique.add(i)
            del d[i]
    d["unique"]=unique
    print(d)

#main
s=input("Enter a sentence: ")
countWords(s)