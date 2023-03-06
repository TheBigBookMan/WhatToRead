from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel

class ToReadDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Dialog that will have the to-read listed, user can add/remove from
        self.setWindowTitle("To Read")
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        layout = QGridLayout()
        title = QLabel("To Read")
        layout.addWidget(title, 0, 0, 1, 2)

        self.setLayout(layout)