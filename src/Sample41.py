class Character:
	"""docstring for Character"""
	def __init__(self, name):
		self.name = name

	def show_profile(self):
		profile = '名前{0}種族：Character'.format(self.name)
		print(profile)

class Monster(Character):
	def __init__(self,name):
		super().__init__(name)
		self.hp = 20

	def show_profile(self):
		profile = '名前{0}種族：Monster HP:{1}'.format(self.name, self.hp)
		print(profile)


monster_a = Monster('モンスターA')
monster_a.show_profile()
