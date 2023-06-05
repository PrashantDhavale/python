class Timer:
    display = ''

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        display = ''
        if self.hour < 10:
            display += '0' + str(self.hour)
        else:
            display += str(self.hour)

        if self.minute < 10:
            display += ':0' + str(self.minute)
        else:
            display += ':' + str(self.minute)

        if self.second < 10:
            display += ':0' + str(self.second)
        else:
            display += ':' + str(self.second)
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


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
for i in range(62):
    timer.prev_second()
    print(timer)
