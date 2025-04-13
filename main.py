import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        pass

    def playTurn(self, row , col):
        pass

    def checkWinner(self):
        pass

    def isboardFull(self):
        pass

    def updateStatus(self):
        pass

    def resetGame(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())


if __name__ =='__main__':
    main()