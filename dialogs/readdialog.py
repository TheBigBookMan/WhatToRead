from PyQt6.QtWidgets import QDialog

class ReadDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Dialog that will have the Read listed, user can add/remove from