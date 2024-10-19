# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    BOOK_TYPES = ("HARDCOVER","PAPERBACK","EBOOK")
    
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None
    
    # TODO: create a static method
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist
    
    # TODO: create a class method
    @classmethod
    def get_book_types(cls):
        return cls.BOOK_TYPES
    


    # the __init__ function is called when the instance is created
    # and ready to be initialized 
    def __init__(self, title,booktype):
        self.title = title
        # TODO: add properties
        # self.auther = author
        # self.pages = pages
        # self.price = price
        # self.__secret = "this is a secret attribute"
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a value book type")
        else:
            self.booktype = booktype

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self,newtitle):
        self.title = newtitle

    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount
    

    # TODO: Properties defined at the class level are shared by all instances



    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount


    


# TODO: access the class attribute
print("Book types: ", Book.get_book_types())


# TODO: Create some book instances
# book1 = Book("Brave New World","Leo Tolstoy",1225,39.95)
# book2 = Book("War and Peace","JD Salinger",234,29.95)
b1 = Book("title1","HARDCOVER")
b2 = Book("title2","PAPERBACK")

# Print the class and property
# print(book1)
# print(book1.title)

# # Print the price of book1
# print(book1.getprice())

# # Try setting the discount
# print(book2.getprice())
# book2.setdiscount(0.25)
# print(book2.getprice())

# # TODO: double-underscore properties are hidden from other classes
# print(book2._Book__secret)



# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)

