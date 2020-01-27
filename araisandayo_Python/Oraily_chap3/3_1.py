# 3-1
years_list = [1993, 1994, 1995, 1996, 1997]

# 3-2
print(years_list[3])

# 3-3
print(years_list[4])

# 3-4
things = ["mozzarella", "cinderella", "salmonella"]

# 3-5
print(things[1].title())

# 3-6
print(things[0].upper())

# 3-7
things.remove("salmonella")
print(things)

# 3-8
surprise = ["Groucho", "Chico", "Harpo"]

# 3-9
surprise2 = surprise[2].lower()
surprise2 = surprise[::-1]
surprise2 = surprise[0].title()
print(surprise2)

# 3-10
e2f = { "dog" : "chien", "cat" : "chat", "warlus" : "morse" }

#3-11
print(e2f['warlus'])

#3-12
f2e = e2f.items()

#3-13
print(e2f['dog'])

#3-14
cats = ['Henri', 'Grumpy', 'Lucy']
animals = {'cats' : cats, 'octopi' : "octopi", 'emus' : "emus"}
life = {'animals' : animals, 'plants' : "plants", 'other' : "other"}

#3-15
print(life.keys())

#3-16
print(life['animals'].keys())

#3-17
print(life['animals']['cats'])

#3-18
empty_set = set(e2f.keys())
print(empty_set)