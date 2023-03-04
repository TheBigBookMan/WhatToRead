from PyQt6.QtWidgets import QDialog

class ExitDialog(QDialog):
    def __init__(self):
        super().__init__
        # ? Just a window that asks if the user wants to exit with yes or no and then no stays on the app and yes closes the app
