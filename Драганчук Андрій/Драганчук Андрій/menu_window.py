from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QButtonGroup, QGroupBox, QLineEdit, QLabel, QApplication, QWidget,  QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox)



card_width, card_height = 500, 500
main_win = QWidget()



batton = QLabel ('ведіть запитання: ')
batton_vin = QLabel ('ведіть вірну відповідь: ')
batton1 = QLabel ('ведіть першу хибну відповідь: ')
batton2 = QLabel ('ведіть другу хибну відповідь: ')
batton3 = QLabel ('ведіть третю хибну відповідь: ')

battons = QLineEdit()
battons_vin = QLineEdit()
battons1 = QLineEdit()
battons2 = QLineEdit()
battons3 = QLineEdit()

lb_stat = QLabel('Статистика')
lb_stats = QLabel()

V1_text = QVBoxLayout()
V1_text.addWidget(batton)
V1_text.addWidget(batton_vin)
V1_text.addWidget(batton1)
V1_text.addWidget(batton2)
V1_text.addWidget(batton3)

V1_texts = QVBoxLayout()
V1_texts.addWidget(battons)
V1_texts.addWidget(battons_vin)
V1_texts.addWidget(battons1)
V1_texts.addWidget(battons2)
V1_texts.addWidget(battons3)

vr_ques = QHBoxLayout()
vr_ques.addLayout(V1_text)
vr_ques.addLayout(V1_texts)

btn_beck = QPushButton('Назад')







main_win.show()