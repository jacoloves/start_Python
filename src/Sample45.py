class Person:
	"""docstring for Person"""
	def __init__(self, name):
		self.name = name

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self,value):
		if not value:
			value = '名無しの権兵衛'
		self._name = value

person = Person('')
print(person.name)
		