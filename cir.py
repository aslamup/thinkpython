import math
def cir_area(xc,yc,xp,yp):
	dx=xp-xc
	dy=yp-yc
	dsquare=dx**2 + dy**2
	r=math.sqrt(dsquare)
	result=math.pi*r**2
	return result
print cir_area(1,2,4,6)
	
