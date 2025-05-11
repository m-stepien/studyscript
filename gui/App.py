from PySide6.QtWidgets import (
     QWidget, QPushButton, QFileDialog, QVBoxLayout, QTextEdit, QProgressBar
)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("StudyScript")
        self.setMinimumSize(600, 400)
        my_pixmap = QPixmap(":/app_icon.png")
        my_icon = QIcon(my_pixmap)
        self.setWindowIcon(my_icon)

        layout = QVBoxLayout()

        self.button_select = QPushButton("Wybierz plik MP4")
        self.button_select.clicked.connect(self.select_file)
        layout.addWidget(self.button_select)

        self.progress = QProgressBar()
        layout.addWidget(self.progress)

        self.transcript_output = QTextEdit()
        self.transcript_output.setReadOnly(True)
        layout.addWidget(self.transcript_output)

        self.setLayout(layout)

    def select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Wybierz plik video", "", "MP4 Files (*.mp4)")
        if file_path:
            self.progress.setValue(10)
            self.transcribe_video(file_path)

    def transcribe_video(self, path):
        self.progress.setValue(50)
        self.transcript_output.setPlainText("Transkrypcja w toku...\n(To będzie prawdziwy tekst)")
        self.progress.setValue(100)