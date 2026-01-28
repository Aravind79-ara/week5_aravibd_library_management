from library_system.library import Library
from library_system.book import Book
from library_system.member import Member

def test_library_borrow():
    lib = Library()
    lib.add_book(Book("Python", "Aravind", "111"))
    lib.register_member(Member("User", "M01"))

    status, _ = lib.borrow_book("111", "M01")
    assert status is True
