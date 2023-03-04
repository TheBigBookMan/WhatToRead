from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatToRead")
        self.setMinimumSize(800, 600)

        #* Create menu bar
        file_menu_item = self.menuBar().addMenu('&File')
        edit_menu_item = self.menuBar().addMenu('&Edit')
        help_menu_item = self.menuBar().addMenu('&Help')

        favourites_action = QAction("Favourites", self)
        file_menu_item.addAction(favourites_action)
        favourites_action.triggered.connect(self.favourites)

        to_read_action = QAction("To Read", self)
        file_menu_item.addAction(to_read_action)
        to_read_action.triggered.connect(self.to_read)
        
        currently_reading_action = QAction("Currently Reading", self)
        file_menu_item.addAction(currently_reading_action)
        currently_reading_action.triggered.connect(self.currently_reading)

        read_action = QAction("Read", self)
        file_menu_item.addAction(read_action)
        read_action.triggered.connect(self.read)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about)


    def favourites(self):
        # ? Input creating a widget here for the user to see favourites that they have favourites etc
        pass

    def to_read(self):
        # ? create the widget for their to-read selection
        pass
    
    def currently_reading(self):
        # ? create the widget for user to see their currently reading section
        pass

    def read(self):
      # ? create widget for user to see their read reading section
      pass

    def about(self):
        dialog = AboutDialog()
        dialog.exec()



class AboutDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """This application allows users to search for books based on title or genre and then add them to their favourites and then select if they want to read/currently reading or read.
        """
        self.setText(content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
    