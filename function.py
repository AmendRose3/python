def calc(tot,shipping,dicount):
    total=0
    total=tot+shipping
    total=total*dicount
    print(f"Your total bill is  ${total}")


#positional arguments
calc(100,5,0.1)
#keyword argument
calc(shipping=10,tot=50,dicount=0.1)
#keyword argument always comes after positional argument

