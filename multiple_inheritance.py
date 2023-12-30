#When doing mulitple inheritance, order of the classes matter. 
import json
class Writeable:
    def write(self, data):
        with open(self.filepath, 'w') as f:
            f.write(data)

class Readable:
    def read(self):
        with open(self.filepath, 'r') as f:
            print(f.read())
       
class JSONSerializable:
    def to_json(self):
     print(json.dumps(self.__dict__))  #convert it to a dict json
                  
class Book(Writeable, Readable, JSONSerializable):
    def __init__(self, title, author, filepath):
        self.title = title
        self.author = author
        self.filepath = filepath
        
book = Book(title='New Book', author='Myself', filepath='./book.txt')
book.write('Hello, welcome to my book')
book.read()
book.to_json()