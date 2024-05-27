#!/usr/bin/python
# -*- coding: utf8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
app = QApplication([])
window = QWidget()
window.resize(300,300)
window.setWindowTitle("calc")

dinamik = 0

chisla = [1,2,3,4,5,6,7,8,9,0]


lay_1 = QHBoxLayout()
lay_2 = QHBoxLayout()
lay_3 = QHBoxLayout()
lay_4 = QHBoxLayout()
lay_5 = QHBoxLayout()
lay_7 = QVBoxLayout()
lay_8 = QVBoxLayout()
lay_9 = QHBoxLayout()
lay_10 = QHBoxLayout()




Box_Group = QGroupBox("Калькулятор")
btn1 = QPushButton("1")
btn2 = QPushButton("2")
btn3 = QPushButton("3")
btn4 = QPushButton("4")
btn5 = QPushButton("5")
btn6 = QPushButton("6")
btn7 = QPushButton("7")
btn8 = QPushButton("8")
btn9 = QPushButton("9")
btn10 = QPushButton("0")
btn11= QPushButton("+")
btn12 = QPushButton("-")
btn13 = QPushButton("X")
btn14 = QPushButton("/")
btn15 = QPushButton("С")

vvod = QLabel("Результат: ")
vvod2 = QLabel(str(chisla))
vvod3= QLabel("0")

# Сюда крепим кнопки нижней строки калькулятора(1,2,3,+)
lay_1.addWidget(btn1)
lay_1.addWidget(btn2)
lay_1.addWidget(btn3)
lay_1.addWidget(btn11)

# Сюда крепим кнопки середины(4,5,6,+)
lay_2.addWidget(btn4)
lay_2.addWidget(btn5)
lay_2.addWidget(btn6)
lay_2.addWidget(btn12)
# Сюда крепим кнопки верха(7,8,9,X)
lay_3.addWidget(btn7)
lay_3.addWidget(btn8)
lay_3.addWidget(btn9)
lay_3.addWidget(btn13)

lay_4.addWidget(btn10)
lay_4.addWidget(btn14)

lay_5.addWidget(btn15)

lay_10.addWidget(vvod)
lay_10.addWidget(vvod2)
lay_10.addWidget(vvod3)

lay_7.addLayout(lay_1)
lay_7.addLayout(lay_2)
lay_7.addLayout(lay_3)
lay_7.addLayout(lay_4)
lay_7.addLayout(lay_5)
lay_7.addLayout(lay_10)


Box_Group.setLayout(lay_7)
lay_8.addWidget(Box_Group)
window.setLayout(lay_8)
Box_Group.hide()
def odin():
   if vvod2.text()!="0":
        if vvod2.text()=="1":
            vvod2.setText("11")
   else:
        vvod2.setText("1")
btn1.clicked.connect(odin)

def dva():
    if vvod2.text()!="0":
        if vvod2.text()=="2":
            vvod2.setText("22")
    else:
        vvod2.setText("2")
btn2.clicked.connect(dva)
    




window.show()
app.exec_()


