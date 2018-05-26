members = {}

class Student:
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name
		self.score = {}

	def add_score(self, subject_name, point):
		self.score[subject_name] = point

	def get_score(self, subject_name):
		return self.score.get(subject_name,'その強化はまだ')
		

members['narito'] = Student('narito')
members['saitou'] = Student('saitou')
members['yosida'] = Student('yosida')

print(members)

members['narito'].