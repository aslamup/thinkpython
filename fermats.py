import sys
def check_fermat(a,b,c,n):
	if int(n)<2:
		return "Enter a number greater than 2"
	else:
		if int(a)**int(n) +int(b)**int(n) == int(c)**int(n):
			return "Holy smokes, Fermat was wrong!"
		else:
			return "No,that doesn't work"
print check_fermat(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])
