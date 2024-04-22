def orderList(data):
    for i in range(0,len(data)-1):
        for j in range(i+1,len(data)):
            if data[i][1]<data[j][1]:
                data[i],data[j]=data[j],data[i]
    return data

tup=[('James J',184.75),('Sara Sam',160),('Laurel T',170.5),
       ('Nicholas A',190), ('Leo V',165), ('Hazel P',145)]
d=orderList(tup)
print(d)
