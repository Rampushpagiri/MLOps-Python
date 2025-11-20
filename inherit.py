# #simple inheritance

# ##base class
# class Animal:

#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(f"{self.name} makes a sund")
# ##derived calss
# class Dog(Animal):
#         def __init__(self):
#             self.behaviur = "friendly"
#         def speak(self):
#             print(f"buddy barks. he is very {self.behaviur}")

# # animal = Animal("Generic Animal")
# # animal.speak()

# dog = Dog()
# dog.speak()

##super keyw0rd

#base calss
class Animal:
    def __init__(self):
        self.name = "buddy"
    def speak(self):
        print(f"{self.name} makes a s0und")

## derived class
class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed
    def speak1 (self):
        super().speak()
        print(f"{self.name} barks.It is a {self.breed}")
dog = Dog("gldern retriver")
dog.speak1()
        