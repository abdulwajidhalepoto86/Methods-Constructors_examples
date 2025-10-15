class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

book1 = Book("Python Basics", "Abdul Wajid", 800)
book2 = Book("AI and ML", "Ismail", 1200)
book3 = Book("Data Science", "Ali ", 950)

book1.display_info()
book2.display_info()
book3.display_info()