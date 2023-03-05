from PyQt6.QtWidgets import QDialog

class FavouritesDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Dialog that will have the favourites listed, user can add/remove from