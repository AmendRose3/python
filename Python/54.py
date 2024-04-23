# 54. Efficient Contact List Application with Search and Update Features: Create a data 
# structure for a contact list application where each contact is represented as a tuple 
# with a name, phone number, and email. The application should allow efficient 
# searching and updating of contact information by any of the three fields.
# Amend:("Amend", "1234567890", "Amend@gmail.com")

contacts = {}

def add_contacts(n):
    for _ in range(n):
        name = input("Name of the contact: ")
        phone_number = input("Number of the contact: ")
        email = input("Email of the contact: ")
        # Tuple of contact details
        details = (phone_number, email)
        contacts[name] = details

def find_contact(name):
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone Number: {contacts[name][0]}")
        print(f"Email: {contacts[name][1]}")
    else:
        print("Contact not found.")

n = int(input("Number of contacts to add: "))
add_contacts(n)
name = input("Who are you interested in? ")
find_contact(name)


