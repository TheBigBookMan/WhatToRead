from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton
from PyQt6.QtGui import QAction, QIcon
import sys
from dialogs.searchdialog import SearchDialog
from dialogs.aboutdialog import AboutDialog
from dialogs.exitdialog import ExitDialog
from dialogs.statusdialog import StatusDialog


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

        exit_action = QAction("Exit", self)
        file_menu_item.addAction(exit_action)
        exit_action.triggered.connect(self.exit_app)

        search_action = QAction("Search", self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search)

        add_favourites_action = QAction("Add To Favourites", self)
        edit_menu_item.addAction(add_favourites_action)
        add_favourites_action.triggered.connect(self.add_favourite)

        update_status_action = QAction("Update Status", self)
        edit_menu_item.addAction(update_status_action)
        update_status_action.triggered.connect(self.status)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about)

        
    def add_favourite(self):
        # ? add favourite to the databse by querying SQL database
        pass
    
    def update_status(self):
        # ? Can take in want-to-read/currently-reading/read ad then query the SQL database and update that book to that status
        # ? Rather than having three seperate functions just make this dynamic
        pass

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

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def about(self):
        dialog = AboutDialog()
        dialog.exec()

    def status(self):
        dialog = StatusDialog()
        dialog.exec()

    def exit_app(self):
        dialog = ExitDialog()
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
    