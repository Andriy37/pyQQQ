
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QVBoxLayout, QRadioButton, QHBoxLayout, QMessageBox, QSpinBox,QGroupBox,QButtonGroup

card_width, card_height = 500, 500 
app = QApplication([]) 
main_win = QWidget() 
main_win.show() 
main_win.setWindowTitle("Memory Card") 

btn_Sleep = QPushButton('Відпочинок')
box_Minuted = QSpinBox()
box_Minuted.setValue(30)
btn_menu = QPushButton('меню')
btn_next = QPushButton('відпочити')

RadioGroupBox = QGroupBox ('варіанти відповіді')
RadioGroup = QButtonGroup('')

rdtn_ans1 = QRadioButton('1')
rdtn_ans2 = QRadioButton('2')
rdtn_ans3 = QRadioButton('3')
rdtn_ans4 = QRadioButton('4')

RadioGroup.addButton(rdtn_ans1)
RadioGroup.addButton(rdtn_ans2)
RadioGroup.addButton(rdtn_ans3)
RadioGroup.addButton(rdtn_ans4)

layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans1 = QHBoxLayout()

layout_ans2.addWidget(rdtn_ans1)
layout_ans2.addWidget(rdtn_ans2)
layout_ans3.addWidget(rdtn_ans3)
layout_ans3.addWidget(rdtn_ans4)







app.exec_()


