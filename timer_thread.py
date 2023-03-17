import time
from PySide6.QtCore import *
from mytime import MyTime

class TimerThread(QThread):
    signal_show = Signal(MyTime)

    def __init__(self):
        super().__init__()
        self.time = MyTime(0,15,30)

    def run(self):
        while True:
            self.time.sub_second()
            time.sleep(1)
            self.signal_show.emit(self.time)