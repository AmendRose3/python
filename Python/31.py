import math

def prime(l,u):
    #using SieveOfEratosthenes concept to find the prime number btw u-upperbound l-lowerbound
    prime = [True for i in range(u + 2)]
    prime[0] = False
    prime[1] = False

    for p in range(2, int(math.sqrt(u))+1):
        if prime[p] == True:
            for i in range(p*p, u+1, p):
                prime[i] = False

    for p in range(l, u+1):
        if prime[p]:
            print(p, end=" ")



l = int(input("Lowerbound: "))
u = int(input("Upperbound:"))
prime(l,u)



