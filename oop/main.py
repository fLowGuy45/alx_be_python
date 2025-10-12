from library_system import Book, EBook, PrintBook, Library
from book_class import Book as BasicBook  # Renamed to avoid conflict with Book in library_system

def demo_library_system():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()


def demo_magic_methods():
    # Demonstrating __str__, __repr__, and __del__
    my_book = BasicBook("1984", "George Orwell", 1949)
    print(my_book)           # Uses __str__
    print(repr(my_book))     # Uses __repr__
    del my_book              # Triggers __del__


if __name__ == "__main__":
    print("=== Library System Demo ===")
    demo_library_system()

    print("\n=== Magic Methods Demo ===")
    demo_magic_methods()
