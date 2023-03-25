import time
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from mytime import MyTime

class WorldClockThread(QThread):
    show_signal = Signal(MyTime, MyTime, MyTime)

    def __init__(self):
        super().__init__()
  
    def run(self):
        while True:
            fulltime = datetime.now()
            nowtime = time.strftime("%H:%M:%S")
            splittime = nowtime.split(":")
            iran_time = MyTime(int(splittime[0]), int(splittime[1]), int(splittime[2]))
            germany_iran = MyTime(2, 30, 0)
            germany_time = iran_time.sub_clock(germany_iran)
            usa_iran = MyTime(7, 30, 0) 
            usa_time = iran_time.sub_clock(usa_iran)
            self.show_signal.emit(iran_time, usa_time, germany_time)
            time.sleep(1)
