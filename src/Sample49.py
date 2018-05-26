class A:
	"""docstring for A"""
	def __getitem__(self,key):
		return key

a = A()
print(a[0])