import sys
import time
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader
from mytime import MyTime
from stopwatch_thread import StopWatchThread
from timer_thread import TimerThread
from alarm_thread import AlarmThread
from world_clock_thread import WorldClockThread
from database import Database
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
        self.ui.btn_start_timer.clicked.connect(self.start_timer)
        self.ui.btn_stop_timer.clicked.connect(self.stop_timer)
        self.ui.btn_rst_timer.clicked.connect(self.reset_timer)

        self.thered_timer = TimerThread()
        self.thread_stopwatch = StopWatchThread()
        self.db=Database()
        self.thread_alarm=AlarmThread()
        self.thread_worldclock=WorldClockThread()
        
        self.thread_stopwatch.signal_show.connect(self.show_stopwatch)
        self.thered_timer.signal_show.connect(self.show_timer)
        self.thread_alarm.start()
        self.thered_timer.signal_show.connect(self.notification)

        #self.thread_worldclock.show_signal.connect(self.show_clock)
        #self.thread_worldclock.start()



    #@Slot
    def start_stopwatch(self):
        self.thread_stopwatch.start()

    #@Slot
    def show_stopwatch(self):
        self.ui.lbl_stopwatch.setText(f'{self.thread_stopwatch.time.hour}:{self.thread_stopwatch.time.min}:{self.thread_stopwatch.time.sec}')

    #@Slot
    def stop_stopwatch(self):
        self.thread_stopwatch.terminate()

    #@Slot    
    def reset_stopwatch(self):
        self.thread_stopwatch.reset()

    

    #@Slot
    def start_timer(self):
        if self.thered_timer.time.sec + self.thered_timer.time.min + self.thered_timer.time.hour != 0:
            timer_time = self.ui.lbl_timer.text()
            splittime=timer_time.split(":")
            self.thered_timer.set_time(int(splittime[0]),int(splittime[1]),int(splittime[2]))
            self.thered_timer.start()

    #@Slot
    def show_timer(self):
        self.ui.lbl_timer.setText(str(self.thered_timer.time.hour)+":"+str(self.thered_timer.time.min)+":"+str(self.thered_timer.time.sec))
        if self.thered_timer.time.sec + self.thered_timer.time.min + self.thered_timer.time.hour == 0:
            self.thered_timer.terminate()

    #@Slot
    def stop_timer(self):
        self.thered_timer.terminate()

    #@Slot
    def reset_timer(self):
        self.thered_timer.set_time(0,15,0)
        self.ui.lbl_timer.setText(str(self.thered_timer.time.hour)+":"+str(self.thered_timer.time.min)+":"+str(self.thered_timer.time.sec))

    
    def show_clock(self, ir_time, us_time, de_time):
        self.ui.iran_time.setText(f"{ir_time.hour} : {ir_time.min} : {ir_time.sec}")
        self.ui.usa_time.setText(f"{us_time.hour} : {us_time.min} : {us_time.sec}")
        self.ui.germany_time.setText(f"{de_time.hour} : {de_time.min} : {de_time.sec}")
    

    def read_from_database(self):
        for i in reversed(range(self.ui.gl_alarms.count())): 
            self.ui.gl_alarms.itemAt(i).widget().setParent(None)
        
        alarms = self.db.get_alarms()

        for i in range(len(alarms)):
            new_lable = QLineEdit()
            new_checkbox = QCheckBox()
            new_toolbtn = QToolButton()

            new_lable.setText(alarms[i][1])
            new_lable.setReadOnly(True)
            new_checkbox.setText("")
            if alarms[i][4] == 0:
                new_checkbox.setChecked(True)
            new_toolbtn.setText("🗑")

            self.ui.gl_alarms.addWidget(new_lable, i, 0)
            self.ui.gl_alarms.addWidget(new_checkbox, i, 1)
            self.ui.gl_alarms.addWidget(new_toolbtn, i, 2)
    
            new_checkbox.clicked.connect(partial(self.is_active, alarms[i][0], alarms[i][4]))
            new_toolbtn.clicked.connect(partial(self.delete, alarms[i][0]))




    def new_alarm(self):
        new_title=self.ui.tb_alarm_title.text()
        new_hour = self.ui.hour_box.text()
        new_min = self.ui.min_box.text()
        feedback = self.db.add_new_task(new_title, new_hour, new_min)
        if feedback == True:
            self.read_from_database()
            self.ui.tb_alarm_title.setText("")
            self.ui.hour_box.setValue(0)
            self.ui.min_box.setValue(0)
            self.thread_alarm.update()
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a prublem")
            msg_box.exec_()

    def is_active(self, id, is_active):
        feedback = self.db.is_active(int(id), int(is_active))
        if feedback == True:
            self.read_from_database()
            self.thread_alarm.update()
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a problem")
            msg_box.exec_()

    def delete(self, id):
        feedback = self.db.remove(int(id))
        if feedback == True:
            self.read_from_database()
            self.thread_alarm.update()
        else:
            msg_box = QMessageBox()
            msg_box.setText("There is a problem")
            msg_box.exec_()

    








if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    main_window.show()

    app.exec()