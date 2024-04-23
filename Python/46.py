occurance = {}

def count_Word(Mainstr):
    global occurance 
    strlist = Mainstr.split(" ")
    for word in strlist:
        if word in occurance:
            occurance[word] += 1
        else:
            occurance[word] = 1  # Change this to 1 instead of 0

def display():
    global occurance
    for word, count in occurance.items():
        print(f"{word}: {count}")

Mainstr = input("Enter a string: ")
count_Word(Mainstr)
display()
