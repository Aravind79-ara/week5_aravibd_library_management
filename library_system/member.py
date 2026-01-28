class Member:
    MAX_BORROW = 5
    FINE_PER_DAY = 5

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
        self.fine_amount = 0

    def borrow_book(self, isbn):
        if len(self.borrowed_books) >= self.MAX_BORROW:
            return False, "Borrow limit reached"
        self.borrowed_books.append(isbn)
        return True, "Book added to member account"

    def return_book(self, isbn):
        if isbn in self.borrowed_books:
            self.borrowed_books.remove(isbn)
            return True, "Book removed from member account"
        return False, "Book not found"
    def add_fine(self, days):
        self.fine_amount += days * self.FINE_PER_DAY

    def clear_fine(self):
        self.fine_amount = 0
        
    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, data):
        member = cls(data["name"], data["member_id"])
        member.borrowed_books = data["borrowed_books"]
        return member

    def __str__(self):
        return f"{self.name} ({self.member_id})"
