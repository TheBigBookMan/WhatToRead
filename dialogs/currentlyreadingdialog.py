from PyQt6.QtWidgets import QDialog, QLabel, QGridLayout

class CurrentlyReadingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Currently Reading")
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        # ? Dialog that will have the currently reading listed, user can add/remove from

        layout = QGridLayout()

        title = QLabel("Currently Reading")
        layout.addWidget(title, 0, 0, 1, 2)

        self.setLayout(layout)