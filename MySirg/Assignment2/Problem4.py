class Book:
    def __init__(self, bookid=None, title=None, price=None):
        self.bookid=bookid
        self.title=title
        self.price=price
    
    def show(self):
        print(f'The book id is: {self.bookid}')
        print(f'The book name is: {self.title}')
        print(f'The price is: {self.price}')

b1=Book('0001', 'Python', '500')
b1.show()

