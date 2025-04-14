import sys
import random
from functools import partial
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QGridLayout,
    QLabel,
    QVBoxLayout,
)


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(300, 300, 600, 600)

        # Set window stylesheet
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                          stop:0 #2c3e50, stop:1 #34495e);
            }
        """)

        self.grid_layout = QGridLayout()
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]

        # Style for buttons
        button_font = QFont('Arial', 36, QFont.Bold)  # Large font for X and O
        for m in range(3):
            for n in range(3):
                self.buttons[m][n].setFixedSize(180, 180)
                self.buttons[m][n].setFont(button_font)
                self.buttons[m][n].setStyleSheet("""
                    QPushButton {
                        background-color: #ecf0f1;
                        border: 2px solid #bdc3c7;
                        border-radius: 10px;
                        color: #2c3e50;
                    }
                    QPushButton:hover {
                        background-color: #dfe6e9;
                    }
                    QPushButton:pressed {
                        background-color: #b2bec3;
                    }
                    QPushButton[text="X"] {
                        color: #e74c3c;
                    }
                    QPushButton[text="O"] {
                        color: #3498db;
                    }
                """)
                self.buttons[m][n].clicked.connect(partial(self.play_turn, m, n))
                self.grid_layout.addWidget(self.buttons[m][n], m, n)
        # Adjust grid layout spacing
        self.grid_layout.setSpacing(10)

        self.status_label = QLabel("Player X's turn")
        self.status_label.setFont(QFont('Arial', 16, QFont.Bold))
        self.status_label.setStyleSheet("""
            QLabel {
                color: #ecf0f1;
                padding: 10px;
            }
        """)
        self.status_label.setAlignment(Qt.AlignCenter)
        self.reset_button = QPushButton("Reset")
        self.reset_button.setFont(QFont('Arial', 14))
        self.reset_button.setStyleSheet("""
            QPushButton {
                background-color: #e67e22;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #d35400;
            }
            QPushButton:pressed {
                background-color: #bf4513;
            }
        """)
        self.reset_button.clicked.connect(self.reset_game)

        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.status_label)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addWidget(self.reset_button)

        self.setLayout(self.v_layout)

        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X" if random.randint(0, 1) == 1 else "O"
        self.update_status()

    def play_turn(self, row, col):
        if self.board[row][col] == "" and not self.check_winner():
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)

            if self.check_winner():
                self.status_label.setText(f"Player {self.current_player} Wins!")
                self.disable_buttons()
            elif self.is_board_full():
                self.status_label.setText("Match Draw!")
                self.disable_buttons()
            else:
                self.current_player = "X" if self.current_player == "O" else "O"
                self.update_status()

    def check_winner(self):
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != "":
                return True

        for col in range(3):
            if (
                self.board[0][col] != ""
                and self.board[0][col] == self.board[1][col] == self.board[2][col]
            ):
                return True

        if self.board[1][1] != "":
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return True
            if self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return True

        return False

    def is_board_full(self):
        return all(self.board[i][j] != "" for i in range(3) for j in range(3))

    def update_status(self):
        self.status_label.setText(f"Player {self.current_player}'s Turn")

    def reset_game(self):
        self.board = [["" for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setText("")
                self.buttons[i][j].setEnabled(True)

        self.current_player = "X" if random.randint(0, 1) == 1 else "O"
        self.update_status()

    def disable_buttons(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].setEnabled(False)


def main():
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
