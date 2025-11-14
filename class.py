#initiliase class
class employee:
    #specila methd/magic functin cnstructor
    def __init__(self):
        print("started executing attr/data")
        self.id = 123
        self.salary = 10000
        self.designation = "SDE"
        print("attr/data have been initiated")

    def travel(self, destination):
        print("this travel methd was called manually")
        print(f" Emplyee travel t {destination}")

# Creating an obj/instance of the class
sam = employee()

#print(sam.designation)
#sam.travel("kerala")
print(type(sam))
