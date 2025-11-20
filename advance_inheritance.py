#single r base inheritance

class Parent:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"hell my name is {self.name}")

#derived calss
class Child(Parent):
        def play(self):
             print(f"{self.name} is playing")
# child = Child("Alice")
# child.greet()
# child.play()    

##multi level inheritance

class Grandparent:
    def __init__(self, name):
          self.name = name
    
    def tell_stry(self):
          print(f"{self.name} tells a stry")

#inherited class
class Parent(Grandparent):
          def wrk(self):
              print(f"{self.name} is wrking")

#Derived class
class Child(Parent):
      def play(self):
            print(f"{self.name} is playing")

child = Child("Charlie")
child.tell_stry()
child.wrk()
child.play()