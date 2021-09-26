# class Dog:
#     tricks = []
#
#     def __init__(self, name):
#         self.name = name
#
#     def add_trick(self, trick):
#         self.tricks.append(trick)
#         return f"{self.name} can {trick}"
#
#
# sharo = Dog("Sharo")
# misho = Dog("Misho")
#
# print(sharo.add_trick("get the ball"))
# print(misho.add_trick("sit down"))
#
# print(sharo.tricks)
# print(misho.tricks)





class Dog:
    tricks = []
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        Dog.tricks.append(trick)
        return f"{self.name} can {trick}"


sharo = Dog("Sharo")
misho = Dog("Misho")

print(sharo.add_trick("get the ball"))
print(misho.add_trick("sit down"))

print(sharo.tricks)
print(misho.tricks)
