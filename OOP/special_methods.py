class Book():
    def __init__(self, name, author, pages):
        self.name = name
        self.author = author
        self. pages = pages
    def __str__(self):
        return f"{self.name} by {self.author}"
    def __len__(self):
        return self.pages

    def __del__(self):
        print("Book object has been deleted")


b = Book('Rose in your heart', 'Yunus Karazak', 200)
print(b)
print(len(b))
print(b)
del b
