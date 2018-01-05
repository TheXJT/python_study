colors=['black','white']
sizes=['S','M','L']
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
	print(tshirt)

a=1
b=2
a,b=b,a
print(a,b)