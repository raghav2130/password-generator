import sys
import pyperclip
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSlider, QPushButton, QCheckBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt, QTimer
from generator import generate_password


class PasswordGeneratorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Password Generator')

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        self.label = QLabel('Select Password Length and Other characters to include:', self)
        layout.addWidget(self.label)

        h_layout = QHBoxLayout()

        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(8)
        self.slider.setMaximum(30)
        self.slider.setValue(12)
        self.slider.setTickInterval(1)
        self.slider.setTickPosition(QSlider.TicksBelow)
        h_layout.addWidget(self.slider) ##

        self.length_label = QLabel('12', self)
        h_layout.addWidget(self.length_label) ##

        h_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum))

        v_layout_checkboxes = QVBoxLayout()

        self.symbols_checkbox = QCheckBox('Include Symbols', self)
        self.symbols_checkbox.setChecked(True)
        v_layout_checkboxes.addWidget(self.symbols_checkbox)
        # h_layout.addWidget(self.lowercase_checkbox)

        self.uppercase_checkbox = QCheckBox('Include Uppercase', self)
        self.uppercase_checkbox.setChecked(True)
        v_layout_checkboxes.addWidget(self.uppercase_checkbox)
        # h_layout.addWidget(self.uppercase_checkbox)

        self.digits_checkbox = QCheckBox('Include Digits', self)
        self.digits_checkbox.setChecked(True)
        v_layout_checkboxes.addWidget(self.digits_checkbox)
        # h_layout.addWidget(self.digits_checkbox)

        h_layout.addLayout(v_layout_checkboxes) ##
        layout.addLayout(h_layout)

        self.slider.valueChanged.connect(self.update_length_label)

        self.generate_button = QPushButton('Generate Password', self)
        self.generate_button.clicked.connect(self.generate_password)
        layout.addWidget(self.generate_button)

        self.setLayout(layout)

    def update_length_label(self, value):
        self.length_label.setText(str(value))

    def generate_password(self):
        length = self.slider.value()
        include_symbols = self.symbols_checkbox.isChecked()
        include_uppercase = self.uppercase_checkbox.isChecked()
        include_digits = self.digits_checkbox.isChecked()

        password = generate_password(length, include_symbols, include_uppercase, include_digits)
        pyperclip.copy(password)
        self.length_label.setText('Generated password has been copied to clipboard')

        QTimer.singleShot(5000, lambda: self.length_label.setText(str(length)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = PasswordGeneratorApp()
    ex.show()
    sys.exit(app.exec_())