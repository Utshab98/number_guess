from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys, pyttsx3,random
from random import randint

speak = pyttsx3.init()

ui,_ = loadUiType("numguess.ui")

class MainApp(QMainWindow,ui):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("text to speech")
        self.actionButton()
        self.ans=0
        self.count=0
    def actionButton(self):
        self.pushButton.clicked.connect(self.input)
        self.pushButton_2.clicked.connect(self.checkans)
        self.pushButton_3.clicked.connect(self.reset_game)
        self.pushButton_4.clicked.connect(self.quit_game)
        self.ans=0
        

    def input(self):
        low = int(self.lineEdit.text())
        high =int(self.lineEdit_2.text())
        ans = randint(low ,high)
        if low=="" or high=="":
            QMessageBox.warning(self,"Blank input","Enter the lowest and highest number")
            speak.say("Enter the two number")
            speak.runAndWait()

        else:
            self.ans= random.randint(int(low),int(high))

    def checkans(self):
        low_range = self.lineEdit.text()
        high_range = self.lineEdit.text()
        guessanswer=self.lineEdit_3.text()
        if self.lineEdit_3=="":
            QMessageBox.warning(self,"Blank input","Please Enter the number you guessed")
            speak.say("Please Enter the guessed  number")
            speak.runAndWait()
        else:
            if int(guess_num)>self.Answer:
                self.count += 1
                speak.say("Guess less than this")
                speak.runAndWait()
                self.lable_4.setText("Guess less than this")
                self.lineEdit_3.setText("")

            elif int("guess_num")<self.answer:
                self.count += 1
                speak.say("Guess higher than this")
                speak.runAndWait()
                self.lable_4.setText("Guess higher than this")
                self.lineEdit_3.setText("")

            
            elif int(guess_num)== self.Answer:
                speak.say("congrates, Finally you Guessed it")
                speak.runAndWait()
                self.lable_4.setText("congratulation! Finally You Guessed it")

            else:
                l = str(low_range)
                h = str(high_range)
                speak.say(f"Error , Number isnot between {l} and {h}")
                speak.runAndWait()
                self.lineEdit_3.setText("")
        self.lable_5.settext("You Tried :" +str(self.count)+" Times")

        
    def reset_game(self):
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineedit_3.setText("")
        self.lable_4.setText("")
        self.lable_5.setText("")
        self.Answer = 0
        

    def quit_game(self):
        speak.say("Quiting game Good bye")
        speak.runAndWait()
        exit()  
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()