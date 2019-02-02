#!/usr/bin/env python
# -*- coding: utf-8 -*-

# create a dict
D1 = {}
D2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
D3 = {'a': 1, 'food': {'b': 2, 'c': 3, 'd': 4}}
D4 = dict.fromkeys(['a', 'b', 'c', 'd'])
D5 = dict(zip(['a', 'b', 'c', 'd'], [1, 2, 3, 4]))
D6 = dict(a = 1, b = 2, c = 3, d = 4)
D7 = D3.copy()
D9 = {x: x**2 for x in range(10)}

print(D1)
print(D2)
print(D3)
print(D4)
print(D5)
print(D6)
print(D7)
print(D9)
# len()
print(len(D2))
# Index
print(D2['a'])
print(D3['food']['b'])
# in .has_key()
print('a' in D2)
# print(D2.has_key('b'))

# .keys() list(.keys())
# .values() list(.values()) 
# .items() list(.items())
print(D2.keys())
print(list(D2.keys()))
print(D2.values())
print(list(D2.values()))
print(D2.items())
print(list(D2.items()))
# .get()
print(D3.get('a'))
print(D3.get('d'))        # there is no key "d" 
print(D3.get('d', 3))
# .update()
D1.update(D2)
print(D1)
# .pop(): 删除 key, 返回 value
print(D2.pop('a'))
# del
del D2['b']
print(D2)
# change
D2['c'] = 5
print(D2)
# &
print(D3.keys() & D4.keys())

