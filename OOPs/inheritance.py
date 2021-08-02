class Dog:
    def walk(self):
        return print("walk")

class Cat(Dog):
  pass
mycat= Cat()
print(mycat.walk())
