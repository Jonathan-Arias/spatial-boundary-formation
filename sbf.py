"""
Matplotlib SBF Model
Built with python 3.6.1, matplotlib, and numpy
Limited functionality, only works with 90 deg and ints for dots

Used as a starting point: 
http://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/

To determine if a point is on a line segment, I used code from: 
http://stackoverflow.com/questions/328107/how-can-you-determine-a-point-is-between-two-other-points-on-a-line-segment#328337

I enhanced my function by adding a threshold, suggested here: 
http://stackoverflow.com/questions/11907947/how-to-check-if-a-point-lies-on-a-line-between-2-other-points/11912171#11912171

author: Jonathan Arias
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib import path
from math import radians
from math import tan
from time import time 

class Point():
	"""Class to represent xy coords"""
	def __init__(self,x,y,num):
		self.x = x
		self.y = y
		self.num = num

def is_between(a, b, c):
	"""Adds a threshold to allow for float calculations"""
	dxc = c.x - a.x
	dyc = c.y - a.y

	dxl = b.x - a.x 
	dyl = b.y - a.y 

	cross = dxc * dyl - dyc * dxl
	return (abs(cross) <= 0.1)

# Angle of line, 90 (vertical) <= theta < 0 (horizontal)
theta = int(input("Please enter a value for theta (0,90]: "))

while theta <= 0:
	theta = int(input("Enter valid angle (0, 90]: "))

# Setup the figure, axis, and plot element (line) to animate
fig = plt.figure()
ax = plt.axes(xlim=(0,10),ylim=(0,10))
line, = ax.plot([],[], linewidth=1, c='red')

# Generate N random (x,y) coords and plot with scatter
N = 100
x = np.random.rand(N)*10
y = np.random.rand(N)*10

plt.scatter(x,y,s=1,c='blue',marker=',')

points = []

for value in range(1,N):
	points.append(Point(x[value],y[value],value))

# Please see angle_diagram.jpg for visual clarification
# Displacement and rotor used to loop line cleanly once reaches end of plot
if theta == 90:
	displacement = 0
	rotor = 10
elif theta == 45:
	displacement = 10
	rotor = 20
else:
	rtheta = radians(theta)
	displacement = 10/tan(rtheta)
	rotor = 10 + displacement
    
# Initialization function: plot the background of each frame
def init():
    line.set_data([],[])
    return line,

# Initialize list to store data (timestamp of line crossing a point, point coords, etc)
record = []

# Save the current time before line starts moving over plot
start_time = time()

# Animation function: this is called sequentially 
def animate(i):
    X = ((i*0.01) % rotor - displacement,(i*0.01) % rotor)
    Y = (0, 10)
    a = Point((i*0.01) % rotor - displacement,0,0)
    b = Point((i*0.01) % rotor,10,0)
    for point in points:
    	if is_between(a, b, point):
    		if not any(item['pointnum'] == point.num for item in record):
    			print("Passed point: " + str(point.num))
    			record.append({'frame': i, 'pointnum': point.num, 'x': point.x, 'y': point.y, 'timestamp': round(time() - start_time, 3)})

    line.set_data(X,Y)
    return line,

# Call the animator, blit=True means only re-draw the parts that have changed
anim = animation.FuncAnimation(fig,animate,init_func = init, 
                               frames = 10000, interval = 1, blit = True)

plt.show()

newfile = 'record.txt'
with open(newfile,'w') as io:
	io.write("Angle: " + str(theta) + "\n")

	for item in record:
		io.write(str(item['x']) + " " + str(item['y']) + " " + str(item['timestamp']) + "\n")
		# io.write("Frame: " + str(item['frame']) + ", pointnum: " + str(item['pointnum']) + ", x: " + str(item['x']) + ", y: " + str(item['y']) + ', timestamp: ' + str(item['timestamp']) + "\n")

	# io.write('\n')

	# for point in points:
	# 	io.write("Pointnum: " + str(point.num) + ", coords: (" + str(point.x) + ", " + str(point.y) + ")\n")