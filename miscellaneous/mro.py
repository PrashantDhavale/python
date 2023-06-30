class Alpha:
    value = "Alpha"

    def say(self):
        return self.value.lower()


class Beta(Alpha):
    value = "Beta"


class Gamma(Alpha):
    def say(self):
        return self.value.upper()


class Delta(Beta, Gamma):
    pass


d = Delta()
b = Beta()

print(d.say() == "BETA")
