class Sub1:
    def first(self):
        print("This is the first function from Sub 1 class.")

class Sub2:
    def second(self):
        print("This is the second function from the Sub 2 class.")

class Super:
    def final(self):
        print("This is the final method from the super class.")


super_obj = Super()
super_obj.final()

sub1_obj = Sub1()
sub1_obj.first()

sub2_obj = Sub2()
sub2_obj.second()
