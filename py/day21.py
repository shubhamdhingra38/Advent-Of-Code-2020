import sys
from collections import defaultdict

with open('./inp.txt') as f:
	contents = f.read()

all_ings = []
bad = set()
map_allergen_to_ing = {}

identified = []

def remove_from_others(allergen, ingy):
	this_ele = next(iter(ingy))
	bad.add(this_ele)
	identified.append((this_ele, allergen))
	for key in map_allergen_to_ing:
		for ele in bad:
			if ele in map_allergen_to_ing[key]:
				map_allergen_to_ing[key].remove(ele)

		if len(map_allergen_to_ing[key]) == 1:
			remove_from_others(key, map_allergen_to_ing[key])


for line in contents.split('\n'):
	ings, allers = line.split(' (contains ')
	ings = set(ings.split(' '))
	allers = allers.strip(')').split(', ')
	for ing in ings:
		all_ings.append(ing)
	
	for allergen in allers:
		if allergen not in map_allergen_to_ing:
			map_allergen_to_ing[allergen] = ings
		else:
			map_allergen_to_ing[allergen] = map_allergen_to_ing[allergen].intersection(ings)
			if len(map_allergen_to_ing[allergen]) == 1:
				remove_from_others(allergen, map_allergen_to_ing[allergen])


print(map_allergen_to_ing)
print(bad)
print()
good_cnt = sum(map(lambda x: x not in bad, all_ings))
print(good_cnt)

print(','.join(x[0] for x in sorted(identified, key=lambda x:(x[1]))))