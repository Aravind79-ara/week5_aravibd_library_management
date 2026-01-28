from .library import Library
from .book import Book
from .member import Member
def admin_login():
    username = input("Admin username: ")
    password = input("Admin password: ")
    return username == "admin" and password == "admin123"

def main():
    library = Library()
    library.load_data()

    while True:
        print("\n=== ARAVIND LIBRARY MANAGEMENT SYSTEM ===")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Year: ")
            library.add_book(Book(title, author, isbn, year))

        elif choice == "2":
            name = input("Member Name: ")
            mid = input("Member ID: ")
            library.register_member(Member(name, mid))

        elif choice == "3":
            isbn = input("ISBN: ")
            mid = input("Member ID: ")
            print(library.borrow_book(isbn, mid)[1])

        elif choice == "4":
            isbn = input("ISBN: ")
            mid = input("Member ID: ")
            print(library.return_book(isbn, mid)[1])

        elif choice == "5":
            key = input("Search keyword: ")
            for book in library.search_books(key):
                print(book)

        elif choice == "6":
            library.save_data()
            print("Data saved. Goodbye!")
            break

if __name__ == "__main__":
    main()
