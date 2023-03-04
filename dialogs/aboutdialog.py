from PyQt6.QtWidgets import QMessageBox

class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """This application allows users to search for books based on title or genre and then add them to their favourites and then select if they want to read/currently reading or read.
        """
        self.setText(content)