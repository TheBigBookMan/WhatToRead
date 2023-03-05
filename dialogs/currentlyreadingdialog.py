from PyQt6.QtWidgets import QDialog

class CurrentlyReadingDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Dialog that will have the currently reading listed, user can add/remove from