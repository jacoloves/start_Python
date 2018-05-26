members = {}

def add_score(name,subject,point):
	student = members.setdefault(name,{})
	student[subject] = point

def get_score(name,subject):
	student = members.get(name)
	if not student:
		return 'いません'
	
	point = student.get(subject)
	if not point:
		return 'その強化はまだです。'

	return point

add_score('narito', 'math', 50)
narito_math = get_score('narito', 'math')
print(narito_math)