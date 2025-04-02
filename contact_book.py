class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact for {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts:
                print(contact)

    def search_contact(self, search_term):
        found = False
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term.lower() in contact.phone or search_term.lower() in contact.email.lower():
                print(contact)
                found = True
        if not found:
            print("No contacts found matching that search term.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact for {name} deleted successfully.")
                return
        print("No contact found with that name.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter the name: ")
            phone = input("Enter the phone number: ")
            email = input("Enter the email address: ")
            contact_book.add_contact(name, phone, email)
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name, phone, or email to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '5':
            print("Exiting the Contact Book.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
