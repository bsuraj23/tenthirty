class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages= pages
    def __str__(self):
        return f"Book Title: {self.title}, Pages: {self.pages}"
    def __len__(self):
        return self.pages
    def __eq__(self, value):
        return self.pages == value.pages
    
#Testing the Book class
book1 = Book("Python Programming", 300)
book2 = Book("Data Science", 400)
book3 = Book("Python Programming", 300)

print(book1)
print(len(book1))  # Output: 300
print(book1 == book2)
