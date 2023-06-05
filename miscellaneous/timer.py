class Timer:
    display = ''

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        display = str(self.hour).zfill(1) + ':' + str(self.minute).zfill(2) + ':' + str(self.second).zfill(2)
        return display

    def next_second(self):
        if self.second >= 59:
            self.second = 0
            self.minute += 1
            if self.minute >= 59:
                self.minute = 0
                self.hour += 1
                if self.hour >= 23:
                    self.hour = 0
        else:
            self.second += 1

    def prev_second(self):
        if self.second == 0:
            self.second = 59
            self.minute -= 1
            if self.minute <= 0:
                self.minute = 59
                self.hour -= 1
                if self.hour <= 0:
                    self.hour = 23
        else:
            self.second -= 1


timer = Timer(23, 1, 59)
print(timer)
timer.next_second()
print(timer)
for i in range(62):
    timer.prev_second()
    print(timer)
