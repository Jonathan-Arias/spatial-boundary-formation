filename = 'record.txt'

with open(filename) as f:
	lines = f.readlines()

angle = lines.pop(0)

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

for item in table:
	print(str(item['x']) + ", " + str(item['y']) + ", " + str(item['t']))
	