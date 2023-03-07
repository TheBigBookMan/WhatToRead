from PyQt6.QtWidgets import QDialog, QGridLayout, QLabel, QRadioButton, QPushButton

class StatusDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Not sure if this can access the update_status function from the main window but if so then yea use that to update the status
        # ? Make this a checkbox with "none", "want to read", "currently reading", "read"
        self.setWindowTitle("Update Book Status")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QGridLayout()
        layout.setContentsMargins(50, 80, 50, 80)
        info = QLabel("Select to update the book status: ")
        layout.addWidget(info)

        self.radio = QRadioButton("None", self)
        self.radio.toggled.connect(self.update)
        layout.addWidget(self.radio)

        self.radio = QRadioButton("To Read", self)
        self.radio.toggled.connect(self.update)
        layout.addWidget(self.radio)

        self.radio = QRadioButton("Currently Reading", self)
        self.radio.toggled.connect(self.update)
        layout.addWidget(self.radio)

        self.radio = QRadioButton("Read", self)
        self.radio.toggled.connect(self.update)
        layout.addWidget(self.radio)

        button = QPushButton("Update")
        button.clicked.connect(self.update_status)
        layout.addWidget(button)

        self.setLayout(layout)

    def update(self):
        self.selected= self.sender().text()

    def update_status(self):
        print(self.selected)
        # ? Need to get the detail from the 
        # ? In here we updte the sql database and then return the user back to main screen
        pass
