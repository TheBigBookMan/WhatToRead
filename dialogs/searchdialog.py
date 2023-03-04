from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton

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
        genres = ["Horror", "Thriller", "Action", "Self-Help"]
        self.book_genre.addItems(genres)
        self.book_genre.setCurrentText(genres[0])
        layout.addWidget(self.book_genre)

        button = QPushButton("Search")
        button.clicked.connect(self.search_for_book)
        layout.addWidget(button)
        self.setLayout(layout)

    def search_for_book(self):
        # ? This will call the api for the books 
        pass