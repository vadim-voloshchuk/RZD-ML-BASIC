class Book():
    def __init__(self, title, author, published_year): 
        self.title = title
        self.author = author
        self.published_year = published_year

    def get_info(self):
        print(f"ваш запрос на книгу:{self.title,self.author,self.published_yearok}")

    def __str__(self):
        return f"название {self.title} автор {self.author}, год выпуска {self.published_year} "


class FictionBook(Book):
    def __init__(self, title, author, published_year, genre):
        super().__init__(title, author, published_year)
        self.genre = genre
        print(f"жанр данной книги:{self.genre}")


class NonFictionBook(Book):
    def __init__(self, title, author, published_year, topic):
        super().__init__(title, author, published_year)
        self.topic = topic
        print(f"тема данной книги:{self.topic}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author, published_year):
        new_book = Book(title, author, published_year)
        self.books.append(new_book)
    
    def list_books(self):
        for book in self.books:
            print(book)


if __name__ == "__main__":
    new_lib = Library()
    new_lib.add_book('Test title', 'test author', 2004)
    new_lib.add_book('Test title', 'test author', 2004)
    new_lib.add_book('Test title', 'test author', 2004)
    new_lib.add_book('Test title', 'test author', 2004)
    new_lib.list_books()

# 3. Реализуйте методы:
#    - `add_book(book)`: добавляет книгу в коллекцию библиотеки,
#    - `remove_book(book)`: удаляет книгу из коллекции библиотеки,
#    - `list_books()`: выводит информацию о всех книгах в библиотеке.