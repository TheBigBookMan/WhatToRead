from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from api import call_google_books

# https://developers.google.com/books/docs/v1/using#PerformingSearch

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
        genres = ["Any", "Antiques & Collectibles", "Architecture", "Art", "Bibles", "Biography & Autobiography", "Body, Mind & Spirit", "Business & Economics", "Comics & Graphic Novels", "Computers", "Cooking", "Crafts & Hobbies", "Design", "Drama", "Education", "Family & Relationships", "Fiction", "Foreign Language Study", "Games & Activities", "Gardening", "Health & Fitness", "History", "House & Home", "Humor", "Language Arts & Disciplines", "Law", "Literary", "Literary Criticism", "Mathematics", "Medical", "Music", "Nature", "Performing Arts", "Pets", "Philosophy", "Photography", "Poetry", "Political Science", "Psychology", "Reference", "Religion", "Science", "Self Help", "Social Science", "Sports & Recreation", "Study Aids", "Technology & Engineering", "Transportation", "Travel", "True Crime", "Young Adult Fiction", "Young Adult Nonfiction"]
        self.book_genre.addItems(genres)
        self.book_genre.setCurrentText(genres[0])
        layout.addWidget(self.book_genre)

        button = QPushButton("Search")
        button.clicked.connect(self.search_for_book)
        layout.addWidget(button)
        self.setLayout(layout)

    def search_for_book(self):
        # ? This will call the api for the books 
        chosen_subject = self.book_genre.itemText(self.book_genre.currentIndex())
        input_title = self.search_book.text()

        if input_title != "" and chosen_subject != "Any":
            input_title = f"{input_title}+"

        if chosen_subject == "Any":
            chosen_subject = ""
        else:
            category = chosen_subject.replace(' ', '+')
            chosen_subject = f"subject:{category}"

        value = input_title + chosen_subject
        book_list = call_google_books(value)
        self.filter_search(book_list)
        
        
    def filter_search(self, list_books):
        print(list_books)
        empty_list = []

        for item in list_books:
            book_dict = {}
            book_dict['id'] = item['id']
            book_dict['title'] = item['volumeInfo']['title']            
            book_dict['authors'] = item['volumeInfo']['authors']
            book_dict['publishedDate'] = item['volumeInfo']['publishedDate']
            book_dict['description'] = item['volumeInfo']['description']
            book_dict['categories'] = item['volumeInfo']['categories']
            book_dict['image'] = item['volumeInfo']['imageLinks']['thumbnail']
            print(book_dict)

        self.google_books = list_books
        self.close()