class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothrorpe():
    def eats(self):
        return 'campers'

b = Bear()
r = Rabbit()
o = Octothrorpe()

print(b.eats())
print(r.eats())
print(o.eats())