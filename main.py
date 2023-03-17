import sys
import time
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime
from stopwatch_thread import StopWatchThread
from timer_thread import TimerThread
from main_window import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lbl_stopwatch.setText("00:00:00")
        self.ui.btn_start_stopwatch.clicked.connect(self.start_stopwatch)
        self.ui.btn_stop_stopwatch.clicked.connect(self.stop_stopwatch)
        self.ui.btn_rst_stopwatch.clicked.connect(self.reset_stopwatch)
        #self.ui.btn_start_timer.clicked.connect(...)

        self.thered_timer = TimerThread()
        self.thread_stopwatch = StopWatchThread()
        
        self.thread_stopwatch.signal_show.connect(self.show_stopwatch)
        #self.thered_timer.signal_show.connect(...)



    # @Slot
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    # @Slot
    def show_stopwatch(self):
        self.ui.lbl_stopwatch.setText(f'{self.thread_stopwatch.time.hour}:{self.thread_stopwatch.time.min}:{self.thread_stopwatch.time.sec}')

    # @Slot
    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    # @Slot    
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()













if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()