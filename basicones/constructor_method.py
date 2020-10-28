class vegetable:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("Iam eating {}".format(self.name))
    def cooking(self):
        print("Iam cooking {}".format(self.name))
leafy = vegetable('spinach')
leafy.eat()
leafy.cooking()
