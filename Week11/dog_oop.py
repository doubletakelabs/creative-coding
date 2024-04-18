class Dog:
    def __init__(self, name="", breed="", furColor="", age=""):
        self.name = name
        self.breed = breed
        self.furColor = furColor
        self.age = age
        self.teethRemoved = 0
    
    def getDogDetails(self):
        print(f"This dog's name is {self.name}. They are a {self.furColor} {self.breed} and are {self.age} years old. They are missing {self.teethRemoved} teeth.")

    def changeAge(self, a):
        self.age = a
        print(f"{self.name}'s age has been changed to {self.age}.")

    def removeTooth(self):
        self.teethRemoved += 1
        print(f"{self.name}'s missing {self.teethRemoved} teeth.")

myDog1 = Dog("Lad", "cattle dog", "red", 13)
myDog2 = Dog("Joanne", "poodle", "white", 1)

myDog1.getDogDetails()
myDog2.getDogDetails()
  
myDog2.changeAge(8)
  
myDog2.getDogDetails()
  
myDog1.removeTooth()
myDog1.removeTooth()
myDog1.removeTooth()
myDog1.removeTooth()
myDog1.removeTooth()
myDog1.removeTooth()

myDog1.getDogDetails()