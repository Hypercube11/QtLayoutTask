from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
app = QApplication([]) 
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Easy Editor')
main_win.resize(400, 200)

v_main = QVBoxLayout()
main_win.setLayout(v_main)

h_main = QHBoxLayout()
v_main.addLayout(h_main)

h_main_2 = QHBoxLayout()
v_main.addLayout(h_main_2)

b1 = QPushButton('Button 1')
h_main.addWidget(b1)

b2 = QPushButton("Button 2")
h_main.addWidget(b2)

b3 = QPushButton("Button 3")
h_main.addWidget(b3) 

b4 = QPushButton("Button 4")
h_main_2.addWidget(b4)

b5 = QPushButton('Button 5')
h_main_2.addWidget(b5)

app.exec_()
