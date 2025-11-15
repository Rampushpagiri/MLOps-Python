#initiliase class
class employee:
    #specila methd/magic functin cnstructor
    def __init__(self):
        #print(id(self))
        #print("started executing attr/data")
        self.id = 123
        self.salary = 10000
        self.designation = "SDE"
        #print("attr/data have been initiated")

    def travel(self):
        #print(id)
        print("this travel methd was called manually")
        print(f" Emplyee travel t  delhi")

# Creating an obj/instance of the class
sam = employee()
sam.name = "rama"
print(sam.name)
#print(id(sam))
ram = employee()
#print(id(sam))
#print(id(ram))
#print(sam.designation)
#sam.travel("kerala")
#print(type(sam))
#sam.travel()
