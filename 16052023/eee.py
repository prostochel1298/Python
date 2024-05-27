import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class DoctorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Запись к врачу')
        self.resize(300, 200)
        
        self.smirnova_button = QPushButton('Записаться к Смирновой', self)
        self.smirnova_button.clicked.connect(self.smirnova_pressed)
        
        self.petrova_button = QPushButton('Записаться к Петровой', self)
        self.petrova_button.clicked.connect(self.petrova_pressed)
        
        layout = QVBoxLayout()
        layout.addWidget(self.smirnova_button)
        layout.addWidget(self.petrova_button)
        
        self.setLayout(layout)

    def smirnova_pressed(self):
        print("Запись к Смирновой")
        # Здесь можно добавить логику записи к Смирновой

    def petrova_pressed(self):
        print("Запись к Петровой")
        # Здесь можно добавить логику записи к Петровой

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DoctorApp()
    window.show()
    sys.exit(app.exec_())