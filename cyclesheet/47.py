#Q47
def populateDict(data):
    d={}
    for i in data:
        if i[0] not in d:
            d[i[0]]=set()
            d[i[0]].add(i[1])
        else:
            d[i[0]].add(i[1])
    print(d)

#main
d=[('Trials of Apollo','Percy J'),
   ('Harry Potter','Harry Potter'),
   ('Trials of Apollo','Leo V'),
   ('Harry Potter','Ron W'),
   ('Divergent','Four'),
   ('Harry Potter','Hermione G')]
populateDict(d)