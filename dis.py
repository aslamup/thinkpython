import math
def dis(x1,y1,x2,y2):
	dx=x2 - x1
	dy=y2 - y1
	p=dx**2 + dy**2
	d=math.sqrt(p)
	return d
print dis(1,2,4,6)
