class A:
	"""docstring for A"""
	def __init__(self):
		self.__value = 1

class B:
	"""docstring for B"""
	def __init__(self, name):
		super().__init__()
		self.name = name

class C:
	"""docstring for C"""
	def __init__(self, name):
		super().__init__(name)
		self.value = 10
		
		
		