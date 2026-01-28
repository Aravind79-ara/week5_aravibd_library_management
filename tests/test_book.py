from library_system.book import Book

def test_book_checkout():
    book = Book("Python", "Aravind", "123")
    status, _ = book.check_out("M01")
    assert status is True
    assert book.available is False
