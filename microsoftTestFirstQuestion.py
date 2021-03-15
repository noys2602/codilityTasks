class Person:
  def __init__(self, name, age, lname):
    self.name = name
    self.age = age
    self.lastname = lname

  def printname(self):
      print(self.name, self.lastname)

  def myfunc(self):
    print("Hello my name is " + self.name)

  def myfunc2(abc): #self can be named as any name, it just have to be the first paramater
    print("Hello my name is " + abc.name)


p1 = Person("John", 36, "Alton")
p1.myfunc()
print(p1.name)
print(p1.age)
p1.age = 30 #set order

x = Person("John",15, "Doe")
x.printname()


class Student(Person):
    def __init__(self, fname, lname): #ovverides person initiakize
        pass



#x = Student("Mike",15, "Olsen")
#x.printname()

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))