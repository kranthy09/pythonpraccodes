class Human(object):
    def __init__(self, age = 0, nationality = "no nationality", locality = "no locality", *args, **kwargs):
        self.age = age
        self.nationality = nationality
        self.locality = locality

    def speak(self):
        print("Hello, my name is :", self.name)

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def get_locality(self):
        return self.locality


class Food(object):
    def __init__(self, style=None, *args, **kwargs):
        self.style = style

    def get_food_style(self):
        return self.style


class maleperson(Human, Food):
    def __init__(self, name = "", age = "", nationality = "", locality = "", style=""):

        Human.__init__(self, age=age, nationality=nationality, locality=locality)
        Food.__init__(self, style=style)

        # super().__init__(age=age, nationality=nationality, locality=locality, style=style)
        # self.name = name



    def speak(self):
        super().speak();
        print("I am child ", self.name)



bob = maleperson(name="Bob", age=42, nationality="British", locality="Manchester", style="veg")

print(bob.get_locality())


print(bob.__dict__)

class A(object):
    def __init__(self, a=None, b=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Init {} with arguments {}'.format(self.__class__.__name__, (a, b)))

class B(object):
    def __init__(self, q=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('Init {} with arguments {}'.format(self.__class__.__name__, (q)))

class C(A, B):
    def __init__(self):
        super().__init__(a=1, b=2, q=3)

c = C()

print(c.__dict__)

