from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
app = QApplication([]) 
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Easy Editor')
main_win.resize(400, 200)
h_main = QHBoxLayout()
main_win.setLayout(h_main)

h_lain = QPushButton('Button 1')
h_main.addWidget(h_lain)

b2 = QPushButton("Button 2")
h_main.addWidget(b2)

b3 = QPushButton("Button 3")
h_main.addWidget(b3) 
app.exec_()
