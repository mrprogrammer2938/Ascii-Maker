#!/usr/bin/python3
# This App Made By Sina Meysami (Persian)
# Ascii Maker v1.0
#

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUi
import pywhatkit as kit
import sys,os

width = 300
height = 440
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        loadUi("./Form/form.ui",self)
        self.setWindowTitle("Ascii Maker")
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(550,200,width,height)
        self.setFixedSize(width,height)
        
        # Button Signal
        
        self.exit_btn.clicked.connect(self.close)
        self.make_btn.clicked.connect(self.make_ascii)
        self.openfile_btn.clicked.connect(self.open_file)
    
        self.set_statusbar()
        
    def make_ascii(self):
        try:
            image = self.o_file
            save_file = QFileDialog.getSaveFileName(self,caption="Save File",filter="Text File (.txt)")
            ascii_text = kit.image_to_ascii_art(image[0],save_file[0])
            os.system(f"notepad {save_file[0]}")
        except (Exception,):
            self.show_err()
    def open_file(self):
        file = QFileDialog.getOpenFileName(self,caption="Open File",filter="Png File (*.png);;Jpg File (*.jpg)")
        self.o_file = file
        
    def set_statusbar(self):
        status = QStatusBar(self)
        status.showMessage("Ascii Maker v1.0")
        status.setStyleSheet("color: #000;")
        self.setStatusBar(status)
    
    def show_err(self):
        width = 300
        height = 200
        dlg = QDialog()
        dlg.setWindowTitle("Ascii-maker/Error")
        dlg.setWindowIcon(QIcon("icon.png"))
        dlg.setGeometry(500,400,width,height)
        text = QTextEdit(dlg)
        text.resize(width,height)
        text.setReadOnly(True)
        text.setFont(QFont("Arial",20))
        text.setText("Please Open File!")
        rev = dlg.exec_()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Ascii Maker")
    app.setApplicationDisplayName("Black-Software")
    app.setApplicationVersion("v1.0")
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Ascii Maker v1.0
    main()
    