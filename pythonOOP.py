
class Book:

    BOOK_TYPE = ("HARDCOVER","PAPERBACK","EBOOK")

    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPE

    __booklist = None

    def __init__(self, title, author, pageCount, price, booktype):
        self.title = title
        self.author = author
        self.pageCount = pageCount
        self.price = float(price)
        if booktype not in Book.BOOK_TYPE:
            raise ValueError(f"{booktype} is not valid ")
        else:
            self.booktype = booktype

    def returnPrice(self):
        if hasattr (self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setDiscount(self,amount):
        self._discount = amount  #the _ before the attribute is internal to the class and shouldn't be accessed outside the class 

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

class Newspaper:
    def __init__(self,name):
        self.name = name

b1 = Book("Catcher in the Rye", "JD Salinger","234","29.95","PAPERBACK")
b2 = Book("War & Peace","Leo Tolstoy","1225","39.95","EBOOK")
n1 = Newspaper("The New York Times")
n2 = Newspaper("The Deccan Herald")

print(b1.title, b1.returnPrice())

b2.setDiscount(0.25)
print(b2.title, round(b2.returnPrice(),2))

print(type(b1) == type(b2))
print(type(b1)==type(n2))

print(isinstance(b1,Book))
print(isinstance(b2,Newspaper))
print(isinstance(b1,object))

print("Book types",Book.getBookTypes())

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)