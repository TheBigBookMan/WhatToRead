from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QPushButton

class ExitDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exit")
        # ? Just a window that asks if the user wants to exit with yes or no and then no stays on the app and yes closes the app
        
        layout = QGridLayout()
        confirmation = QLabel("Are you sure you want to exit?")
        yes = QPushButton("Yes")
        no = QPushButton("No")

        layout.addWidget(confirmation, 0, 0, 1, 2)
        layout.addWidget(yes, 1, 0)
        layout.addWidget(no, 1, 1)
        self.setLayout(layout)

