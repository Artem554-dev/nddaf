from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QLabel, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox
from random import shuffle




app = QApplication([])
window = QWidget()
window.resize(500,400)

otv = QPushButton("Ответить", window)
otv.move(200,300)
la_qes = QLabel("Вопрос", window)
la_qes.move(200,20)



RadioGroupBox = QGroupBox("Варианты ответа")
rd = QRadioButton("12",window)
rd.move(200,100)
rd1 = QRadioButton("13",window)
rd1.move(300,100)
rd2 = QRadioButton("1",window)
rd2.move(100,200)
rd3 = QRadioButton("2",window)
rd3.move(300,200)

number = 0
all_ans = 0
ri_ans = 0

AnsGroup = QGroupBox("Результаты теста")
la_prav = QLabel('Правельно или нет', window)
la_otv = QLabel('Ответы',window)
la_prav.move(0,0)
la_otv.move(200,200)
sled = QPushButton('Следующий вопрос',window)
sled.move(200,300)

window.setWindowTitle("Memory Card")


class Question():
    def __init__(self, question, right_answer, answer2, answer3, answer4):
        self.question = question
        self.rightanswer = right_answer
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4


question_list = []
question_list.append(Question('press F в какой игре была первой','в call of duty','в Payday 2','',''))

question_list.append(Question('сколько частей сталкер','3','2','1','4'))

question_list.append(Question('сколько надо class-D чтобы почистить камеру scp-173','3','2','4','1'))

question_list.append(Question('сколько парталов может быть одновреммено открыто в portal 2','4','2','1','3'))

question_list.append(Question('Какая часть call of duty была лудшей','modern Warfarem 2','modern Warfarem 4','modern Warfarem','modern Warfarem 3'))

question_list.append(Question('сколько частей метро','4','2','1','3'))

question_list.append(Question('какая видео карта лучшая','3080 ti','2080 ti','3080','2080'))

question_list.append(Question('какой процессор лучший','AMD','intel 7','нет','нет'))

question_list.append(Question('','','','',''))

question_list.append(Question('','','','',''))

question_list.append(Question('','','','',''))

question_list.append(Question('','','','',''))

question_list.append(Question('','','','',''))

question_list.append(Question('','','','',''))

question_list.append(Question('','','','',''))

def Question():
    la_prav.hide()
    la_otv.hide()
    sled.hide()
    rd.show()
    rd1.show()
    rd2.show()
    rd3.show()
    otv.show()
    la_qes.show()

def Answer():
    la_prav.show()
    la_otv.show()
    sled.show()
    rd.hide()
    rd1.hide()
    rd2.hide()
    rd3.hide()
    otv.hide()
    la_qes.hide()

answer = [rd, rd1, rd2, rd3]

def ask(question , rigt_answer, answer2, answer3, answer4):
    shuffle(answer)
    answer[0].setText(rigt_answer)
    answer[1].setText(answer2)
    answer[2].setText(answer3)
    answer[3].setText(answer4)
    la_qes.setText(question)
    la_otv.setText(rigt_answer)
    Question()


def check_answer():
    global all_ans
    global ri_ans
    all_ans += 1
    if answer[0].isChecked():
        ri_ans += 1
        la_prav.setText("Правильно!\n Статистика:"+str(ri_ans)+"/"+str(all_ans))
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            la_prav.setText("Нихтправельно!\n Статистика:"+str(ri_ans)+"/"+str(all_ans))
    Answer()

def next_question():
    global number
    if number >= len(question_list):
        number = 0
    q = question_list[number]
    ask(q.question,q.rightanswer,q.answer2,q.answer3,q.answer4)
    number += 1

window.setWindowTitle("Memory Card")
ask("Варианты ответа","2","1","13","12")
otv.clicked.connect(check_answer)
sled.clicked.connect(next_question)

window.show()
app.exec()