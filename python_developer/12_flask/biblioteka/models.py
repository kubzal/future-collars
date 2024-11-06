class Book:
    def __init__(self, title, author, count):
        self.title = title
        self.author = author
        self.count = count

    def to_dict(self):
        return {"title": self.title, "author": self.author, "count": self.count}
