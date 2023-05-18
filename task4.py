from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
app = QApplication([]) 
main_win = QWidget()
main_win.show()
main_win.setWindowTitle('Easy Editor')
main_win.resize(400, 200)

h_main = QHBoxLayout()
main_win.setLayout(h_main)

v_main = QVBoxLayout()
h_main.addLayout(v_main)

# h_main_2 = QHBoxLayout()
# v_main.addLayout(h_main_2)

b1 = QPushButton('Button 1')
v_main.addWidget(b1)

b2 = QPushButton("Button 2")
v_main.addWidget(b2)

b3 = QPushButton("Button 3")
v_main.addWidget(b3) 

b4 = QPushButton("Button 4")
h_main.addWidget(b4)

v_main_2 = QVBoxLayout()
h_main.addLayout(v_main_2)

b5 = QPushButton('Button 5')
v_main_2.addWidget(b5)

b6 = QPushButton('Button 6')
v_main_2.addWidget(b6)

b7 = QPushButton('Button 7')
v_main_2.addWidget(b7)

app.exec_()
