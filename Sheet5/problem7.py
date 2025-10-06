'''
Q7. Design a Library class that manages:
- Adding new books (title, author, copies)
- Borrowing a book (reduce copies if available)
- Returning a book (increase copies)
'''

class Library():
    def __init__(self):
        self.books = []
        
    def display_books(self):
        if not self.books:
            print("No books available")
        else:
            for book in self.books:
                print(f"All Books\nTitle : {book['title']},\nAuthor: {book['author']},\nCopies: {book['copies']}")
        
    def add_book(self,title,author,copies):
        book = {'title':title,
                'author':author,
                'copies':copies}
        self.books.append(book)
        print(f'Book "{title}" added successfully.')
    
    def borrow_book(self,title):
        for book in self.books:
            if book['title'] == title:
                if book['copies'] > 0:
                    book['copies'] -= 1
                    print(f'You have borrowed "{title}".')
                    return
                else:
                    print(f'Sorry, "{title}" is not available.')
    
    def return_book(self,title):
        for book in self.books:
            if book['title'] == title:
                book['copies'] += 1
                print(f'Thank you for returning "{title}".')
                return
            else:
                print(f'Error: "{title}" does not belong to this library.')
                
                
lib = Library()
lib.add_book("Bhagvad Gita", "Ved Vyas", 3)
lib.add_book("Ramayana", "Valmiki", 2)

lib.borrow_book("Ramayana")
lib.borrow_book("Bhagvad Gita")

lib.return_book("Ramayana")
lib.return_book("Bhagvad Gita")

lib.display_books()