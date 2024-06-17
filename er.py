import sqlite3
from PyQt6.QtWidgets import QApplication, QDialog
from er import Ui_Dialog
# (.venv) PS C:\Users\3-18-5\ИНТЕРФЕЙС\er.py



import sys
myConnection = sqlite3.connect("базза.db")
myCursor = myConnection.cursor()
app = QApplication(sys.argv)
window = QDialog()

er = Ui_Dialog()
er.setupUi(window)

window.show()

def on_click():
    myCursor.execute("select film from films WHERE  _id = 3")
    myResult = myCursor.fetchall()
    print(myResult)
    er.lineEdit.setText(str(myResult))
    er.pushButton_2.setText("xzxzx")
    er.lineEdit.setGeometry(10, 170, 313, 20)





er.pushButton_2.clicked.connect(on_click)





app.exec()
myConnection.close()
