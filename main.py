from PyQt5.QtWidgets import QApplication,QWidget,QLineEdit,QPushButton,QHBoxLayout,QVBoxLayout,QGridLayout
from PyQt5.QtGui import QFont

class CalcApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator App")
        self.resize(260,310)

        self.textbox = QLineEdit()
        self.textbox.setFont(QFont("Helvetica",36))

        self.grid = QGridLayout()
        self.buttons = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "0",".","=","+"
        ]
        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            button.setStyleSheet("QPushButton {font: 30pt Helvetica; padding: 20px;}")
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.delete = QPushButton("<")
        self.clear.setStyleSheet("QPushButton {font: 30pt Helvetica; padding: 15px;}")
        self.delete.setStyleSheet("QPushButton {font: 30pt Helvetica; padding: 15px;}")

        master_layout = QVBoxLayout()
        master_layout.addWidget(self.textbox)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(30,30,30,30)
        self.setLayout(master_layout)

        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)

    def button_click(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.textbox.text()
            try:
                res = eval(symbol)
                self.textbox.setText(str(res))
            except Exception as e:
                print("Error : ",e)
        elif  text == "Clear":
            self.textbox.clear()

        elif text == "<":
            current_value = self.textbox.text()
            self.textbox.setText(current_value[:-1])
        else:
            current_value = self.textbox.text()
            self.textbox.setText(current_value + text)


if __name__ == "__main__":
    app = QApplication([])
    mainWindow = CalcApp()
    mainWindow.setStyleSheet("QWidget { background-color: #bde0fe}")
    mainWindow.show()
    app.exec_()


