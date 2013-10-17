#some simple math fuctions to play with implementing a module or what I would call python library

def add(x,y):
	return x + y

def substract(x,y):
	return x - y

def multiply(x,y):
	return x * y

def exponentiate(base,power):
	ans = 1
	
	for i in range(power):
		ans *= base
	
	return ans
		
def recurseExpon(base,power):
	
	if(power > 1):
		ans = base * recurseExpon(base,power-1)		
		return ans
	elif(power == 1):
		ans = base * 1
		return ans
