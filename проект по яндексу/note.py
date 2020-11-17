import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from PyQt5.QtWidgets import QSizePolicy, QFontDialog, QLabel
from PyQt5.QtWidgets import QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QAction, qApp


class Notepad(QWidget):

    def __init__(self):
        super().__init__()
        self.note = QTextEdit(self)
        self.clear_btn = QPushButton('Clear')
        self.save_btn = QPushButton('Save')
        self.open_btn = QPushButton('Open') 

        self.init_ui()

    def init_ui(self):
        v_layout = QVBoxLayout()
        h_layout = QHBoxLayout()

        h_layout.addWidget(self.clear_btn)
        h_layout.addWidget(self.save_btn)
        h_layout.addWidget(self.open_btn)

        v_layout.addWidget(self.note)
        v_layout.addLayout(h_layout)

        self.save_btn.clicked.connect(self.save_text)
        self.clear_btn.clicked.connect(self.clear_text)
        self.open_btn.clicked.connect(self.open_text)

        self.setLayout(v_layout)
        self.setWindowTitle('PyQt5 TextEdit')
        
        window = QVBoxLayout()
        self.font_action = QPushButton('Font', self)
        self.font_action.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)
        self.font_action.move(1488, 10)
        window.addWidget(self.font_action)
        self.font_action.clicked.connect(self.edit_Font) 
        self.show()
        
    
    def edit_Font(self):
        
        font, ok = QFontDialog.getFont()
        if ok:
            self.note.setFont(font)   
            
    def save_text(self):
        filename = QFileDialog.getSaveFileName(self, 'Save File', 
                                               os.getenv('HOME'))
        try:
            with open(filename[0], 'w') as f:
                my_note = self.note.toPlainText()
                f.write(my_note)
        except:
            None

    def open_text(self):
        filename = QFileDialog.getOpenFileName(self, 'Open File', 
                                               os.getenv('HOME'))
        try:
            with open(filename[0], 'r') as f:
                file_note = f.read()
                self.note.setText(file_note)
        except:
            None

    def clear_text(self):
        self.note.clear()
        
class Write(QMainWindow):
    def __init__(self):
        super().__init__()

        self.form_widget = Notepad()
        self.setCentralWidget(self.form_widget)

        self.init_ui()

    def init_ui(self):
        bar = self.menuBar()
        file = bar.addMenu('File')

        new_action = QAction('New', self)
        new_action.setShortcut('Ctrl+N')

        save_action = QAction('&Save', self)
        save_action.setShortcut('Ctrl+S')

        open_action = QAction('&Open', self)
        open_action.setShortcut('Ctrl+O')

        exit_action = QAction('&Exit', self)
        exit_action.setShortcut('Ctrl+E')
        
        file.addAction(new_action)
        file.addAction(save_action)
        file.addAction(open_action)
        file.addAction(exit_action)
        
        bar_edit = self.menuBar()
        file_edit = bar_edit.addMenu('Edit')        
        
        allocation_action = QAction('&Emphasize', self)
        allocation_action.setShortcut('Ctrl+A')

        copy_action = QAction('&Copy', self)
        copy_action.setShortcut('Ctrl+C')

        paste_action = QAction('&Paste', self)
        paste_action.setShortcut('Ctrl+V')
        
        cut_action = QAction('&Cut', self)
        cut_action.setShortcut('Ctrl+X')        

        remove_action = QAction('&Remove', self)
        remove_action.setShortcut('Ctrl+Z')        
        
        file_edit.addAction(allocation_action)
        file_edit.addAction(copy_action)
        file_edit.addAction(paste_action)
        file_edit.addAction(cut_action)
        file_edit.addAction(remove_action)        
        
        bar1 = self.menuBar()
        file_format = bar1.addMenu('Format')  
        
        font_action = QAction('Font', self)
        file_format.addAction(font_action)
        
        exit_action.triggered.connect(self.exit_trigger)
        file.triggered.connect(self.respond)

        self.show()
        
     
    def exit_trigger(self):
        qApp.quit()

    def respond(self, q):
        signal = q.text()

        if signal == 'New':
            self.form_widget.clear_text()
        elif signal == '&Open':
            self.form_widget.open_text()
        elif signal == '&Save':
            self.form_widget.save_text()


app = QApplication(sys.argv)
writer = Write()
sys.exit(app.exec_())
