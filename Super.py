class Parent():
    def __init__(self,name):
        self.name=name
        print("from parent class",name)
class child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        print("age is",age)

c=child("saniya" , 12)  





         