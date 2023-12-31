from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(QButtonGroup, QGroupBox, QLabel, QApplication, QWidget,  QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox)

app = QApplication([])

card_width, card_height = 500, 500
main_win = QWidget()
main_win.resize(card_width, card_height)
main_win.move(300, 300)
main_win.show()
main_win.setWindowTitle("Memory Card")

btn_sleep = QPushButton("відпочити")
box_minutes = QSpinBox()
box_minutes.setValue(40)

btn_menu = QPushButton("Меню")
btn_OK = QPushButton("Відповісти")
lb_Question = QLabel("Тут буде слово")

RadioGroupBox = QGroupBox("Варіанти відповідей")

RadioGroup = QButtonGroup()

rbtn_ans1 = QRadioButton("1")
rbtn_ans2 = QRadioButton("2")
rbtn_ans3 = QRadioButton("3")
rbtn_ans4 = QRadioButton("4")

RadioGroup.addButton(rbtn_ans1)
RadioGroup.addButton(rbtn_ans2)
RadioGroup.addButton(rbtn_ans3)
RadioGroup.addButton(rbtn_ans4)

AnsGroupBox = QGroupBox("Результат теста")

Lb_Result = QLabel('')
Lb_Correct = QLabel('')

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_ans1)
layout_ans2.addWidget(rbtn_ans2)
layout_ans3.addWidget(rbtn_ans3)
layout_ans3.addWidget(rbtn_ans4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(Lb_Result, alignment=(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop))
layout_res.addWidget(Lb_Correct, alignment= Qt.AlignmentFlag.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)

layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)

layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_Question, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch= 1)
layout_card.addStretch(1)
layout_card.addSpacing(5)

main_win.setLayout(layout_card)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.serText("Наступне питання")

def show_questions():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText("Відповісти")
    RadioGroup.setExclusive(False)
    rbtn_ans1.setChecked(False)
    rbtn_ans2.setChecked(False)
    rbtn_ans3.setChecked(False)
    rbtn_ans4.setChecked(False)
    RadioGroup.setExclusive(True)


main_win.show
app.exec_()