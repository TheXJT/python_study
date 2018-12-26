import itertools

a=itertools.groupby('LLLLAAGGG')
# print(list(a))
# for char,group in a:
	# print(char,'->',list(group))
animals=['duck','eagle','rat','giraffe','bear','bat','dolphin','shark','lion']
animals.sort(key=len)
# print(animals)
for length,group in itertools.groupby(reversed(animals),len):
	print(length,'->',list(group))