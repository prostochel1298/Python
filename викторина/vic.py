from ctypes import alignment
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
app = QApplication([])
window = QWidget()
window.setWindowTitle("Викторина какая-нибудь")
lay1 = QVBoxLayout()
lay2 = QHBoxLayout()
lay3 = QHBoxLayout()
lay4 = QHBoxLayout()
lay5 = QHBoxLayout()
lay6 = QHBoxLayout()
quest = QLabel("Тест на пидОра")
true_btn = QRadioButton("Нажми сюда")
false_btn1 = QRadioButton("Нажми сюда")
false_btn2 = QRadioButton("Нажми сюда")
false_btn3 = QRadioButton("Нажми сюда")

lay2.addWidget(quest,alignment=Qt.AlignCenter)
lay3.addWidget(false_btn2, alignment=Qt.AlignCenter)
lay3.addWidget(true_btn,alignment=Qt.AlignCenter)
lay4.addWidget(false_btn1,alignment=Qt.AlignCenter)
lay4.addWidget(false_btn3,alignment=Qt.AlignCenter)

lay1.addLayout(lay2)
lay1.addLayout(lay3)
lay1.addLayout(lay4)
lay1.addLayout(lay5)
lay1.addLayout(lay6)

window.setLayout(lay1)
def correct():
    cor_win = QMessageBox()
    cor_win.setText("Ты Пидор")
    cor_win.exec_()
def incorrect():
    cor_lose = QMessageBox()
    cor_lose.setText("Ты Пидор")
    cor_lose.exec_()

true_btn.clicked.connect(correct)
false_btn1.clicked.connect(incorrect)
false_btn2.clicked.connect(incorrect)
false_btn3.clicked.connect(incorrect)



window.resize(500,500)
window.show()
app.exec_()

