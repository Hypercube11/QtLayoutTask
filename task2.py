from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
app = QApplication([]) 
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Easy Editor')
main_win.resize(400, 200)

h_main = QHBoxLayout()
main_win.setLayout(h_main)

h_lain = QPushButton('Button 1')
h_main.addWidget(h_lain)

v_main = QVBoxLayout()
h_main.addLayout(v_main)

b3 = QPushButton("Button 3")
h_main.addWidget(b3) 

b4 = QPushButton("Button 4")
v_main.addWidget(b4)

b5 = QPushButton('Button 5')
v_main.addWidget(b5)
b2 = QPushButton("Button 2")
v_main.addWidget(b2)

app.exec_()
