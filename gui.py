from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QAction
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatToRead")
        self.setMinimumSize(800, 600)

        #* Create menu bar
        file_menu_item = self.menuBar().addMenu('&File')
        edit_menu_item = self.menuBar().addMenu('&Edit')
        about_menu_item = self.menuBar().addMenu('&About')

        


    def about(self):
        dialog = AboutDialog()
        dialog.exec()


class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This application allows users to search for books based on title or genre and then add them to their favourites and then select if they want to read/currently reading or read.
        """
        self.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
    