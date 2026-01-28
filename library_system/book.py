from datetime import datetime, timedelta

class Book:
    """Represents a book in the library"""

    def __init__(self, title, author, isbn, year=None):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.duedate = None

    def check_out(self, member_id, loan_period=12):
        """Borrow the book"""
        if not self.available:
            return False, "Sorry! Book already borrowed"

        self.available = False
        self.borrowed_by = member_id
        self.duedate = (datetime.now() + timedelta(days=loan_period)).strftime("%Y-%m-%d")
        return True, f"Book borrowed successfully. Due date: {self.duedate}"

    def return_book(self):
        """Return the book"""
        if self.available:
            return False, "Book is already in the library"

        overdue = self.is_overdue()
        self.available = True
        self.borrowed_by = None
        self.duedate = None

        return True, "Book returned (Overdue)" if overdue else "Book returned successfully"

    def is_overdue(self):
        """Check if the book is overdue"""
        if self.duedate:
            return datetime.now() > datetime.strptime(self.duedate, "%Y-%m-%d")
        return False

    def days_overdue(self):
        """Calculate number of overdue days"""
        if self.is_overdue():
            due = datetime.strptime(self.duedate, "%Y-%m-%d")
            return (datetime.now() - due).days
        return 0

    def to_dict(self):
        """Convert Book object to dictionary for JSON storage"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "duedate": self.duedate
        }

    @classmethod
    def from_dict(cls, data):
        """Create Book object from dictionary"""
        book = cls(
            data["title"],
            data["author"],
            data["isbn"],
            data.get("year")
        )
        book.available = data["available"]
        book.borrowed_by = data["borrowed_by"]
        book.duedate = data["duedate"]
        return book

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} ({self.isbn}) - {status}"
