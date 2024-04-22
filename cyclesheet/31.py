def listPrimes(l,h):
    lp=[]
    for i in range(l,h+1):
        f=1
        for j in range(2,i):
            if i%j==0:
                f=0
                break
        if f==1:
            lp.append(i)
    return lp

#main
print("Enter range")
l=int(input("Lower range: "))
h=int(input("Upper range: "))
primes=listPrimes(l,h)
print("Primes in the range: ",primes)
        

