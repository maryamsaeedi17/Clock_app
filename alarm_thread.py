#import time
from datetime import datetime
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from mytime import MyTime
from database import Database


class AlarmThread(QThread):
    signal_show = Signal(str, int, int)

    def __init__(self):
        super().__init__()
        self.db = Database()
        self.alarms = self.db.get_alarms()
  
    def run(self):
        while True:
            for i in range(len(self.alarms)):
                if self.alarms[i][4] == 0:
                    alarm = MyTime(self.alarms[i][2], self.alarms[i][3], 0)
                    fulltime = datetime.now()
                    nowtime = fulltime.strftime("%H:%M")
                    splittime = nowtime.split(":")
                    time = MyTime(int(splittime[0]), int(splittime[1]), 0)
                    if time.same_time(alarm) == True:
                        self.signal_show.emit(self.alarms[i][1], self.alarms[i][2], self.alarms[i][3])

    
    def update(self):
        self.alarms = self.db.get_alarms()