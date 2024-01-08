#While loop,nested if-else
print("Lets Drive! ")
print("""Command Menu:
1.start
2.stop
3.exit
      
      """)
cmd=" "
started=False
while True:
    cmd=input("> ")
    if cmd.lower()=="start":
        if started==False:
            print("Car Started ...")  
            started=True
        else:
            print("Car is already started bro...")  
    elif cmd.lower()=="stop":
        if started==True:
            print("Car Stopped ...") 
            started=False
        else:
           print("Car is already stopped bro...")   
    elif cmd.lower()=="exit":
        break
    else:
        print("Command not recognized") 

print("Byeee!!! ")
