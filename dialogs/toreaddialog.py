from PyQt6.QtWidgets import QDialog

class ToReadDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Dialog that will have the to-read listed, user can add/remove from