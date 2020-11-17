import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QLCDNumber, QLabel, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
 
    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Калькулятор')
        
        self.name_label = QLabel(self)
        self.name_label.setText('Введите первое число: ')
        self.num = QLineEdit(self)
        self.num.move(20, 20)
        
        self.name_label1 = QLabel(self)
        self.name_label1.setText('Введите второе число: ')
        self.name_label1.move(0, 40)
        self.num1 = QLineEdit(self)
        self.num1.move(20, 60)
       
        
        self.error = QLabel(self)
        self.error.setText('                             ')
        self.error1 = QLabel(self)
        self.error1.setText('                             ')
        self.error2 = QLabel(self)
        self.error2.setText('                             ')
        self.error3 = QLabel(self)
        self.error3.setText('                             ')
        self.error4 = QLabel(self)
        self.error4.setText('                             ')
        
                   
        self.btn = QPushButton(self)
        self.btn.move(80, 90)
        self.btn.setText('Рассчитать')
        self.btn.clicked.connect(self.calculate)
 
        self.LCD_sum = QLCDNumber(self)
        self.LCD_sum.move(100, 120)
        self.LCD_substr = QLCDNumber(self)
        self.LCD_substr.move(100, 150)
        self.LCD_mult = QLCDNumber(self)
        self.LCD_mult.move(100, 180)
        self.LCD_div = QLCDNumber(self)
        self.LCD_div.move(100, 210)
        
    def calculate(self):
        x, y = int(self.num.text()), int(self.num1.text())
        self.error.setText('')
        self.error1.setText('')
        self.error2.setText('')
        self.error3.setText('')
        self.error4.setText('')
        if y != 0:
            if len(str(x + y)) > 5:
                self.error1.setText('TooLong')
                self.error1.move(200,120)
            else:
                self.LCD_sum.display(x + y)
            if len(str(x - y)) > 5:
                self.error2.setText('TooLong')
                self.error2.move(200,150)
            else:
                self.LCD_substr.display(x - y)
            if len(str(x * y)) > 5:
                self.error3.setText('TooLong')
                self.error3.move(200,180)
            else:
                self.LCD_mult.display(x * y)
            if len(str(x / y)) > 5:
                self.error4.setText('TooLong')
                self.error4.move(200,210)
            else:
                self.LCD_div.display(x / y)             
        else:
            self.error.setText('Ошибка!!')
            self.error.move(100,250)  
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())