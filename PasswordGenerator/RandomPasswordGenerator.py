import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit
import random

class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')
        self.setGeometry(300, 300, 400, 300)

        self.layout = QVBoxLayout()

        self.label_complexity = QLabel('Password Complexity:')
        self.input_complexity = QLineEdit(self)

        self.label_number = QLabel('Number of Passwords:')
        self.input_number = QLineEdit(self)

        self.label_length = QLabel('Password Length:')
        self.input_length = QLineEdit(self)

        self.generate_button = QPushButton('Generate Passwords', self)
        self.generate_button.clicked.connect(self.generate_passwords)

        self.password_display = QTextEdit(self)
        self.password_display.setReadOnly(True)

        self.layout.addWidget(self.label_complexity)
        self.layout.addWidget(self.input_complexity)
        self.layout.addWidget(self.label_number)
        self.layout.addWidget(self.input_number)
        self.layout.addWidget(self.label_length)
        self.layout.addWidget(self.input_length)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.password_display)

        self.setLayout(self.layout)

    def generate_passwords(self):
        complexity = self.input_complexity.text()
        number = int(self.input_number.text())
        length = int(self.input_length.text())

        chars = self.get_character_set(complexity)

        generated_passwords = []
        for _ in range(number):
            password = self.generate_password(chars, length)
            generated_passwords.append(password)

        self.password_display.setPlainText('\n'.join(generated_passwords))

    def generate_password(self, chars, length):
        return ''.join(random.choice(chars) for _ in range(length))

    def get_character_set(self, complexity):
        if complexity == 'easy':
            return 'abcdefghijklmnopqrstuvwxyz'
        elif complexity == 'medium':
            return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        elif complexity == 'strong':
            return 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec_())
