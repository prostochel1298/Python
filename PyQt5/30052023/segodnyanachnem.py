# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
app = QApplication([])
window = QWidget()
window2=QWidget()
window.resize(500, 500)
window.setWindowTitle("ОднерОчка")
lay1= QVBoxLayout()
lay2= QHBoxLayout()
lay3= QHBoxLayout()
lay4= QHBoxLayout()
lay5=QHBoxLayout()
lay6=QHBoxLayout()
bg = QGroupBox()
laylay = QVBoxLayout()


cereal = QPushButton("Крупа")
drinks = QPushButton("Напитки")
meal = QPushButton("Мясо")
preserve = QPushButton("Консервы")
bread = QPushButton("Хлеб")

lay2.addWidget(cereal,alignment=Qt.AlignLeft)
lay3.addWidget(drinks,alignment=Qt.AlignLeft)
lay4.addWidget(meal,alignment=Qt.AlignLeft)
lay5.addWidget(preserve,alignment=Qt.AlignLeft)
lay6.addWidget(bread,alignment=Qt.AlignLeft)
lay1.addLayout(lay2)
lay1.addLayout(lay3)
lay1.addLayout(lay4)
lay1.addLayout(lay5)
lay1.addLayout(lay6)
bg.setLayout(lay1)
laylay.addWidget(bg)
window.setLayout(laylay)
bg.show()




def cereals():
    bg.hide()
    rice = QLabel("Рис")
    buckwheat = QLabel("Гречка")
    pearl = QLabel("Перловая крупа")
    semolina = QLabel("Манная крупа")
    lay2.addWidget(rice,alignment=Qt.AlignCenter)
    lay3.addWidget(buckwheat,alignment=Qt.AlignCenter)
    lay4.addWidget(pearl,alignment=Qt.AlignCenter)
    lay5.addWidget(semolina,alignment=Qt.AlignCenter)
    lay1.addLayout(lay2)
    lay1.addLayout(lay3)
    lay1.addLayout(lay4)
    lay1.addLayout(lay5)
   
cereal.clicked.connect(cereals)

window.show()
app.exec_()






