from PyQt6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QToolBar
from PyQt6.QtGui import QAction, QIcon
import sys
from dialogs.searchdialog import SearchDialog
from dialogs.aboutdialog import AboutDialog
from dialogs.exitdialog import ExitDialog
from dialogs.statusdialog import StatusDialog
from dialogs.favouritesdialog import FavouritesDialog
from dialogs.toreaddialog import ToReadDialog
from dialogs.currentlyreadingdialog import CurrentlyReadingDialog
from dialogs.readdialog import ReadDialog


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
        favourites_action.triggered.connect(self.open_favourites)

        to_read_action = QAction("To Read", self)
        file_menu_item.addAction(to_read_action)
        to_read_action.triggered.connect(self.open_to_read)
        
        currently_reading_action = QAction("Currently Reading", self)
        file_menu_item.addAction(currently_reading_action)
        currently_reading_action.triggered.connect(self.open_currently_reading)

        read_action = QAction("Read", self)
        file_menu_item.addAction(read_action)
        read_action.triggered.connect(self.open_read)

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

        # Create navbar toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)

        to_favourites = QAction("Favourites", self)
        to_favourites.triggered.connect(self.open_favourites)
        toolbar.addAction(to_favourites)

        to_to_read = QAction("To Read", self)
        to_to_read.triggered.connect(self.open_to_read)
        toolbar.addAction(to_to_read)

        to_currently_reading = QAction("Currently Reading", self)
        to_currently_reading.triggered.connect(self.open_currently_reading)
        toolbar.addAction(to_currently_reading)

        to_read = QAction("Read", self)
        to_read.triggered.connect(self.open_read)
        toolbar.addAction(to_read)


        
    def add_favourite(self):
        # ? add favourite to the databse by querying SQL database
        pass
    
    def update_status(self):
        # ? Can take in want-to-read/currently-reading/read ad then query the SQL database and update that book to that status
        # ? Rather than having three seperate functions just make this dynamic
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

    def open_favourites(self):
        dialog = FavouritesDialog()
        dialog.exec()

    def open_to_read(self):
        dialog = ToReadDialog()
        dialog.exec()

    def open_currently_reading(self):
        dialog = CurrentlyReadingDialog()
        dialog.exec()

    def open_read(self):
        dialog = ReadDialog()
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
    