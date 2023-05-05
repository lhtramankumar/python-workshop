class A :
   def __init__(self, name,age) :
    self.name =name 
    self.age =age
    
   def details(self) :
    return self.name

p1 = A("Raman",20)
print(p1.details())

class B:
   def __init__(self, name,id) :
    self.name =name 
    self.id =id
   def details(self) :
    return self.name

p2 =B ("Test","sadlkajdkl44k9skkjsfd")
print(p2.details())


class C(A):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_details(self) :
        return self.name

c = C("Raman", 20)
print(c.get_details())