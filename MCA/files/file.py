data = '''
23MCA0001 aaa 01-01-2002 9.5
23MCA0002 abc 04-07-2003 9.4
23MCA0003 bcd 13-07-2001 7.1
23MCA0004 cde 24-02-2002 6.8
23MCA0005 def 25-04-2002 9.8
23MCA0006 feg 03-09-2001 8.5
23MCA0007 ghi 01-06-2001 9.1
23MCA0008 hij 10-02-2001 8.7
23MCA0009 ijk 13-03-2001 7.8
23MCA0010 jkl 17-01-2001 9.8
'''

with open('alltxt.txt',"w") as fh:
    fh.write(data)
    
details=[]

with open('alltxt.txt',"r") as fh:
    for i in fh:
        details.append(i.split())
print(details)

with open('above9.txt',"w") as ab:
    for i in details:
        if float(i[3]) >= 9.0:
            print(F"{i[0]} {i[1]}")
            ab.write(F"{i[0]} {i[1]}\n")

with open('below9.txt',"w") as ab:
    for i in details:
        if float(i[3]) <= 9.0:
            print(F"{i[0]} {i[1]}")
            ab.write(F"{i[0]} {i[1]}\n")