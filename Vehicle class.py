class Vehicle():
    def __init__(self, name = "", kind = "", color = "", value = ""):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth %s." % (self.name, self.color, self.kind, self.value)
        return desc_str


car1 = Vehicle("ferrari", "convertible", "red", "$60000")
#car1.name = "ferrari"
#car1.kind = "convertible"
#car1.color = "red"
#car1.value = "$60,000"

car2 = Vehicle("Jump", "covertible", "black", "$100000")
#car2.name = "Van"
#car2.kind = "convertible"
#car2.color = "black"
#car2.value = "$10,000"

print(car1.description())
print(car2.description())

