import json
from .book import Book
from .member import Member

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, isbn, member_id):
        if isbn not in self.books or member_id not in self.members:
            return False, "Invalid book or member"

        book = self.books[isbn]
        member = self.members[member_id]

        success, msg = book.check_out(member_id)
        if success:
            member.borrow_book(isbn)
        return success, msg

    def return_book(self, isbn, member_id):
       book = self.books.get(isbn)
       member = self.members.get(member_id)

       if not book or not member:
          return False, "Invalid data"

       overdue_days = book.days_overdue()
       success, msg = book.return_book()

       if overdue_days > 0:
        member.add_fine(overdue_days)
        msg += f" | Fine added: ₹{member.fine_amount}"

        member.return_book(isbn)
       return success, msg
 

    def search_books(self, keyword):
        keyword = keyword.lower()
        return [
            book for book in self.books.values()
            if keyword in book.title.lower()
            or keyword in book.author.lower()
            or keyword in book.isbn
        ]

    def save_data(self):
        with open("data/books.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f, indent=4)

        with open("data/members.json", "w") as f:
            json.dump({k: v.to_dict() for k, v in self.members.items()}, f, indent=4)

    def load_data(self):
        try:
            with open("data/books.json") as f:
                books = json.load(f)
                for k, v in books.items():
                    self.books[k] = Book.from_dict(v)
        except FileNotFoundError:
            pass

        try:
            with open("data/members.json") as f:
                members = json.load(f)
                for k, v in members.items():
                    self.members[k] = Member.from_dict(v)
        except FileNotFoundError:
            pass
