from .book import Book

class Member:
    def __init__(self, name: str):
        # TODO: Initialize member with a name and empty checked-out list
        pass

    def checkout(self, book: Book) -> None:
        # TODO: Add book to checked-out list
        pass

    def return_book(self, isbn: str) -> bool:
        # TODO: Remove book with given ISBN if present
        pass

    def list_checked_out(self) -> list:
        # TODO: Return the list of checked-out books
        pass
