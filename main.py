from inventory import LibraryInventory

def main():
    inventory = LibraryInventory()

    while True:
        print("\nMenu:")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            if inventory.add_book(title, author, isbn):
                print("Book added.")
            else:
                print("Book with this ISBN already exists.")

        elif choice == "2":
            isbn = input("Enter ISBN to issue: ")
            book = inventory.find_book(isbn)
            if book and book.issue():
                print(f"Issued '{book.title}'.")
            else:
                print("Cannot issue book (not found or already issued).")

        elif choice == "3":
            isbn = input("Enter ISBN to return: ")
            book = inventory.find_book(isbn)
            if book and book.return_book():
                print(f"Returned '{book.title}'.")
            else:
                print("Cannot return book (not found or already available).")

        elif choice == "4":
            inventory.display_all()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid input, try again.")

if __name__ == "__main__":
    main()
