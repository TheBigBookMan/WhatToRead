from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel

class FavouritesDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Dialog that will have the favourites listed, user can add/remove from
        self.setWindowTitle("Favourites")
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        layout = QGridLayout()
        title = QLabel("Favourites")
        layout.addWidget(title, 0, 0, 1, 2)

        self.setLayout(layout)