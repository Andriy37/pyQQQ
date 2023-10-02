from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout,QRadioButton,QVBoxLayout,QMessageBox
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс від крейзі піопле?')
text = QLabel('в якому році канал отрмав золоту кнопку від Ютубе?')
text1 = QRadioButton('2005')
winner1 = QRadioButton('2015')
winner2 = QRadioButton('2010')
winner3 = QRadioButton('2020')

line = QVBoxLayout()
line.addWidget(text, alignment = Qt.AlignCenter)
line.addWidget(text1, alignment = Qt.AlignCenter)
line.addWidget(winner1, alignment = Qt.AlignCenter)
line.addWidget(winner2, alignment = Qt.AlignCenter)
line.addWidget(winner3, alignment = Qt.AlignCenter)


layH1 = QHBoxLayout()
layH2 = QHBoxLayout()
layH3 = QHBoxLayout()
layH1.addWidget(text, alignment = Qt.AlignCenter)
layH2.addWidget(text1, alignment = Qt.AlignCenter)
layH2.addWidget(winner1, alignment = Qt.AlignCenter)
layH3.addWidget(winner2, alignment = Qt.AlignCenter)
layH3.addWidget(winner3, alignment = Qt.AlignCenter)
layo_win = QVBoxLayout()
layo_win.addLayout(layH1)
layo_win.addLayout(layH2)
layo_win.addLayout(layH3)
main_win.setLayout(layo_win)

def show_win ():
    vict_win = QMessageBox()
    vict_win.setText("правильно!\n ви виграли")
    vict_win.exec_()
def show_so ():
    vict_win = QMessageBox()
    vict_win.setText("ні не правильно в 2015 році")
    vict_win.exec_()

winner1.clicked.connect(show_win)
winner2.clicked.connect(show_so)
winner3.clicked.connect(show_so)
text1.clicked.connect(show_so)

main_win.show()
app.exec_()