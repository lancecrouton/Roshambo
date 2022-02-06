# importing libraries
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("Roshambo ")

        # Set size of game window
        self.setGeometry(200, 200, 640, 800)

        # Call UI method for display
        self.user_interface()

        # Show widgets
        self.show()

    def user_interface(self):  # Method to show UI interface

        # counter variable
        self.counter = -1

        # choice variable
        self.choice = 0

        # Game title
        head = QLabel("Roshambo", self)

        # Center game title
        head.setGeometry(40, 20, 560, 120)

        # Select font
        font = QFont('Fantasy', 15)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)

        # Set font to game title
        head.setFont(font)

        # Set alignment to game title
        head.setAlignment(Qt.AlignCenter)

        # Set color to game title
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.black)
        head.setGraphicsEffect(color)

        # Add vs. text
        self.vs = QLabel("vs", self)

        # Align vs. text
        self.vs.setGeometry(300, 220, 60, 100)

        # Select font
        font.setUnderline(False)
        font.setItalic(False)
        self.vs.setFont(font)

        # Create player label
        self.user = QLabel("Player", self)

        # Set player box
        self.user.setGeometry(100, 200, 140, 140)
        self.user.setStyleSheet("border : 2px solid black; background : blue;")

        # Align user box
        self.user.setAlignment(Qt.AlignCenter)

        # Create computer label
        self.computer = QLabel("Computer", self)

        # Set computer box
        self.computer.setGeometry(400, 200, 140, 140)
        self.computer.setStyleSheet("border : 2px solid black; background : red;")

        # Align computer box
        self.computer.setAlignment(Qt.AlignCenter)

        # Create result label
        self.result = QLabel(self)

        # Set result label
        self.result.setGeometry(50, 400, 540, 100)

        # Set result label font
        self.result.setFont(QFont('Times', 14))

        # Align result label
        self.result.setAlignment(Qt.AlignCenter)

        # Set border and color
        self.result.setStyleSheet("border : 2px solid black; background : white;")

        # Create button for rock, paper and scissors
        self.rock = QPushButton("Rock", self)
        self.rock.setGeometry(60, 540, 160, 70)

        self.paper = QPushButton("Paper", self)
        self.paper.setGeometry(240, 540, 160, 70)

        self.scissor = QPushButton("Scissor", self)
        self.scissor.setGeometry(420, 540, 160, 70)

        # Add actions to buttons
        self.rock.clicked.connect(self.rock_action)
        self.paper.clicked.connect(self.paper_action)
        self.scissor.clicked.connect(self.scissor_action)

        # Create reset button
        game_reset = QPushButton("Reset", self)

        # Center reset button
        game_reset.setGeometry(200, 640, 240, 100)

        # Set color effect
        color = QGraphicsColorizeEffect(self)
        color.setColor(Qt.red)
        game_reset.setGraphicsEffect(color)

        # Add action to reset button
        game_reset.clicked.connect(self.reset_action)

        # Create timer
        timer = QTimer(self)

        # Add action to timer
        timer.timeout.connect(self.showTime)

        # Start timer
        timer.start(1000)

    def showTime(self):

        # if counter value is - 1
        if self.counter == -1:
            pass

        # if counter is not - 1
        else:

            # setting counter value to the label
            self.computer.setText(str(self.counter))

            if self.counter == 0:
                self.comp_choice = random.randint(1, 3)

                # if computer choice is 1
                if self.comp_choice == 1:

                    # setting rock image to the computer label
                    self.computer.setStyleSheet("border-image : url(RockCPU.png);")

                elif self.comp_choice == 2:
                    # setting paper image to the computer label
                    self.computer.setStyleSheet("border-image : url(PaperCPU.png);")

                else:
                    # setting scissor image to the computer label
                    self.computer.setStyleSheet("border-image : url(ScissorCPU.png);")

                # checking who won the match
                self.who_won()

            # decrementing the counter value
            self.counter -= 1

    def rock_action(self):

        # making choice as 1
        self.choice = 1

        # setting rock image to the user label
        self.user.setStyleSheet("border-image : url(RockPlayer.png);")

        # making counter value to 3
        self.counter = 3

        # disabling the push button
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)

    def paper_action(self):

        # making choice as 2
        self.choice = 2

        # setting rock image to the user label
        self.user.setStyleSheet("border-image : url(PaperPlayer.png);")

        # making counter value to 3
        self.counter = 3

        # disabling the push button
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)

    def scissor_action(self):

        # making choice as 3
        self.choice = 3

        # setting rock image to the user label
        self.user.setStyleSheet("border-image : url(ScissorPlayer.png);")

        # making counter value to 3
        self.counter = 3

        # disabling the push button
        self.rock.setDisabled(True)
        self.paper.setDisabled(True)
        self.scissor.setDisabled(True)

    def reset_action(self):

        # making result label empty
        self.result.setText("")

        # resting the counter value
        self.counter = -1

        # enabling the push buttons
        self.rock.setEnabled(True)
        self.paper.setEnabled(True)
        self.scissor.setEnabled(True)

        # removing images fro the user and computer label
        self.user.setStyleSheet("border-image : null;")
        self.computer.setStyleSheet("border-image : null;")

    def who_won(self):

        # if match is draw
        if self.choice == self.comp_choice:

            # setting text to the result label
            self.result.setText("Draw Match")

        else:
            # condition for winning
            # user choose rock
            if self.choice == 1:
                # computer choose paper
                if self.comp_choice == 2:
                    # setting text to the result
                    self.result.setText("Computer Wins")
                else:
                    self.result.setText("User Wins")

            # user chooses paper
            elif self.choice == 2:
                # computer choose scissor
                if self.comp_choice == 3:
                    # setting text to the result
                    self.result.setText("Computer Wins")
                else:
                    self.result.setText("User Wins")

            # if user chooses scissor
            elif self.choice == 3:
                # computer choose rock
                if self.comp_choice == 1:
                    # setting text to the result
                    self.result.setText("Computer Wins")
                else:
                    self.result.setText("User Wins")


# Create pyqt app
App = QApplication(sys.argv)

# Create instance
window = Window()

# Start app
sys.exit(App.exec())
