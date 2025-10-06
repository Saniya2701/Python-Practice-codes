
#single inheritance

class parent:
    def home(self):
        print("parent")

class child(parent):
    pass

c=child()
c.home()

#-----------------------------------------------
#multilevel

class grandparent:
    def home(self):
        print("grandparent")

class parent(grandparent):
    def car(self):
        print("parent")

class child(parent):
    pass

c=child()
c.car()
c.home()


#-------------------------------------------------------------
#multiple

class father:
    def home(self):
        print("father home")

class mother:
    def care(self):
        print("mother care")

class child(father,mother):
    pass

c=child()
c.care()
c.home()

#-----------------------------------------------------------

#hierarchical

class grandparent:
    def home(self):
        print("grandparent home")

    def car(self):
        print("grandparent car")

class parent(grandparent):
    pass

class child(grandparent):
    pass

c=child()
c.home()
c.car()


#-------------------------------------------
#hybrid

class animal:
    def eat(self):
        print("eats")

    def sleep(self):
        print("sleep")

class dog(animal):
    def leg(self):
        print("have legs")

class fish(animal):
    def swim(self):
        print("swims")       
          
class tuna(fish):
    def fins(self):
        print("have fins")


t=tuna()
t.fins()
t.swim()

f=fish()
f.eat()
f.sleep()
f.swim()

d=dog()
d.eat()
d.sleep()
d.leg()
