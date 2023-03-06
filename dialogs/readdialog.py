from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel

class ReadDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Dialog that will have the Read listed, user can add/remove from
        self.setWindowTitle("Read")
        self.setFixedWidth(500)
        self.setFixedHeight(500)

        layout = QGridLayout()
        title = QLabel("Read")
        layout.addWidget(title, 0, 0, 1, 2)

        self.setLayout(layout)