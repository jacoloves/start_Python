class Person:
	"""docstring for Person"""
	def __init__(self, name):
		self.origin_name = name
		self.name = name

	@property
	def name(self):
		return self.real_name
	
	@name.setter
	def name(self,value):
		if not value:
			value = '名無しの権兵衛'
		self.real_name = value

person = Person('田中')
print(person.name)
person = Person('')
print(person.name)
		