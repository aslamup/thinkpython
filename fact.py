def fact(n):
	if n==0:
		return 1
	else:
		r=factorial(n-1)
		result=n*r
		return result
fact(4)
	
