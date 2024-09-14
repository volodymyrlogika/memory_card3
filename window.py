from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QPushButton, QSpinBox, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout


window = QWidget() # створення вікна
window.setWindowTitle("Memory Card") #назва вікна
window.resize(500, 500) # змінити розмір вікна
window.move(200,200) #положення вікна 

# Перший ряд кнопок
menu_btn = QPushButton("Меню")
rest_btn = QPushButton("Відпочити")
time_box = QSpinBox()
time_label = QLabel("хвилин")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addStretch(1)
row1.addWidget(rest_btn)
row1.addWidget(time_box)
row1.addWidget(time_label)

# Напис з запитанням
question_text = QLabel("mouse")


main_line = QVBoxLayout()
main_line.addLayout(row1)
main_line.addWidget(question_text, alignment=Qt.AlignCenter)

btn1 = QRadioButton("миша")
btn2 = QRadioButton("щур")
btn3 = QRadioButton("мішок")
btn4 = QRadioButton("мус")

answer_btn = QPushButton("Відповісти")

window.setLayout(main_line)
