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

#Hierarchical inheritance
#base calss
class Parent:
    def __init__(self, name):
            self.name = name
    def greet(self):
            print(f"hellp my name is {self.name}")

#derived class 1
class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing")

#derived class 2
class Child2(Parent):
    def study(self):
            print(f"{self.name} is studying")


child1 = Child1("Dave")
child2 = Child2("Eve")

child1.greet()
child1.play()

child2.greet()
child2.study()

##multiple inheritance

class A:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"hellp frm A, {self.name}")
#interndetiate class 1
class B(A):
    def greet(self):
         print(f"hell frm B, {self.name}")
         super().greet()

#interndetiate class 2
class C(A):
    def greet(self):
         print(f"hell frm C, {self.name}")
         super().greet()
# Derived class
class D(B, C):
     def greet(self):
          print(f"Hell frm D, {self.name}")
    
          super().greet()
#create an instance f D

d = D("frank")
d.greet()


#Hybrid inheritance
#base class
class Animal:
     def __init__(self, name):
          self.name = name
     def sund(self):
          print(f"{self.name} make a sund")

#inheritclass 1 (hirarchical)
class Mamam(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk")

#inheritate class 2 (multiple)
class Bird(Animal):
     def fly(self):
          print(f"{self.name} is flying")
#Derived class (multile inheritance)
class Bat(Mamam, Bird):
    def __init__(self, name):
          Mamam.__init__(self, name)
    def natural(self):
     print(f"{self.name} is natuaral")

#create instance f Bat
bat = Bat("ram")
bat.sund()
bat.feed()
bat.fly()
bat.natural()
          