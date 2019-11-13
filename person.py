class Person(object):
	def __init__(self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def eat(self,):
		print(self.name + " is drinking a smoothie")
	def mood(self):
		print(self.name + "'s mood is scheisse!")
person1 = Person("Mark",34,"Bayern","male")
person1.eat()
person1.mood()