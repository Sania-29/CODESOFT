# Contact Management System

contacts = []

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    key = input("Enter name or phone to search: ").lower()
    found = False

    for contact in contacts:
        if key in contact['name'].lower() or key in contact['phone']:
            print("\nContact Found:")
            print(contact)
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    phone = input("Enter phone number of contact to update: ")

    for contact in contacts:
        if contact['phone'] == phone:
            print("Enter new details (leave blank to keep old value)")
            name = input(f"New Name ({contact['name']}): ")
            email = input(f"New Email ({contact['email']}): ")
            address = input(f"New Address ({contact['address']}): ")

            if name:
                contact['name'] = name
            if email:
                contact['email'] = email
            if address:
                contact['address'] = address

            print("Contact updated successfully!")
            return

    print("Contact not found.")

def delete_contact():
    phone = input("Enter phone number of contact to delete: ")

    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("Contact deleted successfully!")
            return

    print("Contact not found.")

def menu():
    print("\n===== CONTACT MANAGEMENT SYSTEM =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

while True:
    menu()
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Management System!")
        break
    else:
        print("Invalid choice. Please try again.")
