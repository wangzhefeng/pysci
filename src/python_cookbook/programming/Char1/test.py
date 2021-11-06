
# -*- coding: utf-8 -*-

__author__ = "wangzhefeng"

# example 1

bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
people = [bob, sue]

for person in people:
	print(person)

for person in people:
	print(person[0].split()[-1])
	person[2] *= 1.20

for person in people:
	print(person[2])

pays1 = [person[2] for person in people]
pays2 = map(lambda x: x[2], people)
sum(person[2] for person in people)
people.append(['Tom', 50, 0, None])
people.extend([['tinker wang', 29, 15000, 'analysist'],
			   ['alvin wang', 20, 0, None]])




# example 2
NAME, AGE, PAY, JOB = range(4)
bob = ['Bob Smith', 42, 30000, 'software']
sue = ['Sue Jones', 45, 40000, 'hardware']
print(bob[NAME])
print(bob[AGE])
print(bob[PAY])
print(bob[JOB])



# example 3
bob = [['name', 'Bob Smith'], ['age', 42], ['pay', 10000]]
sue = [['name', 'Sue Jones'], ['age', 45], ['pay', 20000]]
people = [bob, sue]

for person in people:
	print(person)
	for (name, value) in person:
		if name == 'name':
			print(value)


def field(record, label):
	for(fname, fvalue) in record:
		if fname == label:
			return fvalue

field(bob, 'name')
field(sue, 'age')
for rec in people:
	print(field(rec, 'age'))



# example 4
bob = {
	'name': 'Bob Smith',
	'age': 42,
	'pay': 30000,
	'job': 'dev'
}
sue = {
	'name': 'Sue Jones',
	'age': 45,
	'pay': 40000,
	'job': 'hdw'
}

print(bob['name'], sue['pay'])
