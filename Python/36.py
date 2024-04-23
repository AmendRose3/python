# 36.Contact Book Application with Multiple Functionalities: Develop a contact book application in Python that enables users to add new 
# contacts, display specific contact details, update contact details, delete a contact, list all contacts, and exit the application.
# Each contact should have a unique Contact ID, name, phone number, and email address. The program should use a dictionary to store 
# contact details and provide a user-friendly menu for interaction.
# Amend:("Amend", "1234567890", "Amend@gmail.com")

contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = (phone_number, email)
    print("Contact added successfully.")

def update_contact():
    name = input("Enter name of the contact to update: ")
    if name in contacts:
        phone_number = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = (phone_number, email)
        print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def find_contact():
    name = input("Enter name of the contact to find: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone Number: {contacts[name][0]}")
        print(f"Email: {contacts[name][1]}")
    else:
        print("Contact not found.")

def list_all_contacts():
    if contacts:
        print("List of all contacts:")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone Number: {details[0]}, Email: {details[1]}")
    else:
        print("No contacts found.")

# Main program loop
while True:
    print("\nContact Book Application")
    print("1. Add contact")
    print("2. Update contact")
    print("3. Delete contact")
    print("4. Find contact")
    print("5. List all contacts")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        update_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        find_contact()
    elif choice == "5":
        list_all_contacts()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 6.")
