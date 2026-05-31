class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"Title : {self.title}\nAuthor : {self.author}\nPrice : {self.price}"

title = input("Enter book title: ")
author = input("Enter author name: ")
price = float(input("Enter book price: "))

b1 = Book(title, author, price)

print("\nBook Details")
print(b1)