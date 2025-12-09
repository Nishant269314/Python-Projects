is_run = True
books = {}  # book name → content


def add_book():
    global books
    print("\n******** Add Book ********")

    name = input("Enter book name: ")
    content = input("Enter book content: ")

    books[name] = content
    print("Book added successfully!\n")


def read_book():
    print("\n******** Read Book ********")

    name = input("Enter book name: ")

    if name in books:
        print("\n--- Book Content ---")
        print(books[name])
        print("---------------------\n")
    else:
        print("Book not found!\n")


def remove_book():
    global books
    print("\n******** Delete Book ********")

    name = input("Enter book name to delete: ")

    if name in books:
        del books[name]
        print("Book deleted!\n")
    else:
        print("Book not found!\n")


while is_run:
    print("*****************************")
    print("          LIBRARY           ")
    print("*****************************")
    print("1. Add Book")
    print("2. Read Book")
    print("3. Delete Book")
    print("4. Exit")
    print("*****************************")

    choice = input("Enter your choice (1,2,3,4): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        read_book()
    elif choice == "3":
        remove_book()
    elif choice == "4":
        print("\nGoodbye!\n")
        break
    else:
        print("Invalid choice! Try again.\n")
