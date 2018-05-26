members = {}

def add_score(name,point):
	members[name] = point

def get_score(name):
	return members.get(name,'いません')

add_score('narito',50)
narito_score = get_score('narito')
print(narito_score	)