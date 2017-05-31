from math import *
from statistics import harmonic_mean

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

def computePhi(p1,p2):
	"""Find angle formed between horizontal line passing through p1 and line connecting p1 to p2"""
	phi = atan2(p2['y']-p1['y'], p2['x'] - p1['x'])
	return phi

def computeVelocity(p1, p2):
	"""Find the magnitude of the transformation vector between p1 and p2"""
	area = sqrt(pow(p2['x'] - p1['x'], 2) + pow(p2['y'] - p1['y'], 2))
	time = p2['t'] - p1['t']
	if time == 0: 
		return 0 # If time difference is 0, points were occluded at same time
	velocity = area / time
	return velocity

def computeAngle(phi_ij, phi_jk, v_ij, v_jk):
	"""Find the orientation of the illusory edge"""
	numerator = v_jk*sin(phi_jk) - v_ij*sin(phi_ij)
	denominator = v_jk*cos(phi_jk) - v_ij*cos(phi_ij)
	theta = atan(numerator/denominator)
	theta = degrees(theta)
	return abs(theta)

maxindex = len(table) - 2
angles = []
velocities = []

# Iterate through data and collect all possible angles/velocities
for i in range(0,maxindex):
	p1= table[i]
	p2 = table[i+1]
	p3 = table[i+2]

	phi_12 = computePhi(p1,p2)
	v_12 = computeVelocity(p1,p2)

	phi_23 = computePhi(p2,p3)
	v_23 = computeVelocity(p2,p3)

	angle = computeAngle(phi_12, phi_23, v_12, v_23)
	angles.append(angle)
	if i == 0: # Only on the first run will we store v_12 to avoid storing duplicates
		velocities.append(v_12)
	velocities.append(v_23)

# Find average of all angles collected
angle_average = round(harmonic_mean(angles),1)
print(str(angle_average))

# Remove zeroes from velocities list
velocities = [x for x in velocities if x != 0]

# Find average of all velocities collected
velocity_average = round(harmonic_mean(velocities),1)
print(str(velocity_average))