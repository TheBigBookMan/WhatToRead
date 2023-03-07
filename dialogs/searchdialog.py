from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from api import call_google_books

class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Books")
        self.setFixedWidth(300)
        self.setFixedHeight(150)

        layout = QVBoxLayout()
        self.search_book = QLineEdit()
        self.search_book.setPlaceholderText("Search Book Title")
        layout.addWidget(self.search_book)

        self.book_genre = QComboBox()
        # !!!! COPY AND PASTE THE GENRES FROM THE API
        genres = ["Any", "Horror", "Thriller", "Action", "Self-Help"]
        self.book_genre.addItems(genres)
        self.book_genre.setCurrentText(genres[0])
        layout.addWidget(self.book_genre)

        button = QPushButton("Search")
        button.clicked.connect(self.search_for_book)
        layout.addWidget(button)
        self.setLayout(layout)

    def search_for_book(self):
        # ? This will call the api for the books 
        book_list = call_google_books("mans+search+for+meaning")
        self.filter_search(book_list)
        chosen_subject = self.book_genre.itemText(self.book_genre.currentIndex())
        
    def filter_search(self, list):
        # print(list)
        pass