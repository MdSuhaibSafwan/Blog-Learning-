class parent():

    def say_name(self):
        print("My name is parent")

    def say_name2(self):
        print("I am a parent")



class Child(parent):

    def say_name(self):
        super().say_name()
        super().say_name2()
        print("My name is child")


c1 = Child()
c1.say_name()
