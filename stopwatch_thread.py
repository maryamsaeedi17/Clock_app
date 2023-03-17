import time
from PySide6.QtCore import *
from mytime import MyTime


class StopWatchThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0,0,0)

    def run(self):
        while True:
            self.time.sum_second()
            time.sleep(1)
            self.signal_show.emit(self.time)

    def reset(self):
        self.time.sec = 0
        self.time.min = 0
        self.time.hour = 0
        self.signal_show.emit(self.time)