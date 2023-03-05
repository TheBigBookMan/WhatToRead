from PyQt6.QtWidgets import QDialog

class StatusDialog(QDialog):
    def __init__(self):
        super().__init__()
        # ? Not sure if this can access the update_status function from the main window but if so then yea use that to update the status
        # ? Make this a checkbox with "none", "want to read", "currently reading", "read"