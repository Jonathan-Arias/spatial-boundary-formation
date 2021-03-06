import pickle
from math import *
from statistics import harmonic_mean

record = []
with open('record.pickle', 'rb') as data:
	record = pickle.load(data)

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
	if denominator == 0:
		denominator = 0.1
	theta = atan(numerator/denominator)
	theta = degrees(theta)
	return abs(theta)

# Process data in groups of three
maxindex = len(record) - 2

angles = []
velocities = []

# Iterate through data and collect all possible angles/velocities
for i in range(0,maxindex):
	p1= record[i]
	p2 = record[i+1]
	p3 = record[i+2]

	phi_12 = computePhi(p1,p2)
	v_12 = computeVelocity(p1,p2)

	phi_23 = computePhi(p2,p3)
	v_23 = computeVelocity(p2,p3)

	angle = computeAngle(phi_12, phi_23, v_12, v_23)
	angles.append(angle)
	if i == 0: # Only on the first run will we store v_12 to avoid storing duplicates
		velocities.append(v_12)
	velocities.append(v_23)

# Remove zeroes from angles list
angles = [x for x in angles if x != 0]

# Find average of all angles collected
angle_average = round(harmonic_mean(angles),1)
print(str(angle_average))

# Remove zeroes from velocities list
velocities = [x for x in velocities if x != 0]

# Find average of all velocities collected
velocity_average = round(harmonic_mean(velocities),1)
print(str(velocity_average))