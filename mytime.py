class MyTime:
    def __init__(self, hh,mm,ss):
        self.hour = hh
        self.min = mm
        self.sec = ss
        self.fix()

    def sum_second(self):
        self.sec += 1
        self.fix()

        
    def sub_second(self):
        self.sec -= 1
        self.fix()

    def show(self):
        print(self.hour,":",self.min,":",self.sec)


    def fix(self):
        if self.sec >= 60:
            while True:
                if self.sec >= 60:
                    self.sec -= 60
                    self.min += 1
                else:
                    break
        if self.min>=60:
            while True:
                if self.min >= 60:
                    self.min -= 60
                    self.hour += 1
                else:
                    break
        if self.sec < 0:
            while True:
                if self.sec < 0:
                    self.sec += 60
                    self.min -= 1
                else:
                    break
        if self.min < 0:
            while True:
                if self.min < 0:
                    self.min += 60
                    self.hour -= 1
                else:
                    break