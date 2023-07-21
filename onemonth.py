class Person:
  def __init__(self, name , age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}{self.age}"
  def myfunc(seft):
    print("hello " + seft.name)
p1 = Person("tu", 21)

p1.myfunc()