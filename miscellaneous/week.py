# ToDo

class WeekDayError(Exception):
    pass


class Weeker:

    def __init__(self, day):
        pass

    def __str__(self):
        pass

    def add_days(self, n):
        pass

    def subtract_days(self, n):
        pass


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
