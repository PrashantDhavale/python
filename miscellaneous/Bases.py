class Un:
    value = "Ein"

    def say(self):
        return self.value.lower()


class Deux(Un):
    value = "Zwei"


class Troi(Un):
    def say(self):
        return self.value.upper()


class Quatre(Troi, Deux):
    pass


d = Quatre()
b = Deux()

print(d.say() == "ZWEI")
print(isinstance(d, Un))
print(Troi in Quatre.__bases__)


