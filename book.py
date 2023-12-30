#Inheritence
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def __str__(self):
        return '<Book: {} by {}'. format(self.title, self.author)

# Inherits Book Class
class TextBook(Book):
    def __init__(self, title, author, edition):
        super().__init__(title, author) # this will run  self.title = title and self.author = author. Calling the base class
        self.edition = edition
 

book = Book(title='All the light', author='Some person')
textbook = TextBook(title='Maths', author='RD Sharma', edition=2)
print(book)
print(textbook)