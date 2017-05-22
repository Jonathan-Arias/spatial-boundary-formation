# This is where sbf.py saves its results
filename = 'record.txt'

with open(filename) as f:
	lines = f.readlines()

# First line will contain the angle supplied in sbf.py
angle = lines.pop(0)

# Store results in list of dicts
table = []
for line in lines:
	li = line.split()
	t = {}
	t['x'] = float(li[0])
	t['y'] = float(li[1])
	t['t'] = float(li[2])
	table.append(t)

print("Success!")
print("Length of table: " + str(len(table)))	