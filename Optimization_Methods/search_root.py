"""
Methods to find the root of a function:
1/Bisection (alpha = 1)
2/Secant (alpha = 1,618...)
3/Newton (alpha = 2)
alpha bigger iff convergence is faster
So why not always use the fastest one?
BECAUSE:
-Newton needs derivative, sometimes we dont want/have it
-Newton and secant are not guaranteed to converge, Bisection method is
So we need to know the 3 methods
"""
def bisection(f, a, b, tol):
	"""
	find the root of a function on a segment [a,b]
	if it exists inside the segment
	and if f(a) and f(b) have different signs
	"""
	low = a
	high = b

	assert f(a)*f(b) < 0

	if f(a) > 0:
		sign_left = 1
	else:
		sign_left = -1

	if (b-a) <= tol:
		return (a + b)/2

	while (high - low) > tol:
		mid = (low + high) / 2
		#we save this val to just do one function call
		#instead of two
		val = f(mid)
		if val == 0:
			break
		elif val*sign_left > 0:
			low = mid
		else:
			high = mid

	return mid

def secant(f, a, b, tol):
	"""
	a and b are just the 2 starting points. The root doesnt have to be inside 
	the segment [a,b]
	BUT: need to pick a and b such as f(a) != f(b)

	algo: we create a sequence x0, x1, ...xn, starting
	with x0 = a and x1 =b, xn converges to the root.
	In this implementation, at each step we just need 
	to store the last 2 elements that we call a and b
	"""
	fa = f(a)
	fb = f(b)
	while abs(fb) > tol:	
		slope = (fb - fa) / (b - a)
		if slope == 0:
			break
		c = b - fb /slope
		# now a moves to b and b moves to c
		a = b
		fa = fb
		b = c
		fb = f(b)

	return b



def newton(f, df, a, tol):
	"""
	df is the derivate of f (can be simple numerical approximation)
	a is just a starting point. Pick it close to the root you want
	and we need f'(a) != 0 

	algo: we create a sequence x_0, x_1, ...x_n, starting
	with x_0 = a and xn converges to the root.
	In this implementation, at each step we just need 
	to store the last element x_n as the point a
	"""
	fa = f(a)

	while abs(fa) > tol:	
		slope = df(a)
		if slope == 0:
			break
		b = a - fa /slope
		# now a moves to b
		a = b
		fa = f(a)

	return a

#example use
def f(x):
	return x**2 - 9

def df(x):
	"""
	approximate the derivate of f
	we could also put here the exact symbolic 
	when it is easy to calculate 
	(here the derivate is just f'(x) = 2*x 
	but it could be a very complicated function)
	"""
	return (f(x + tol) - f(x - tol)) / (2 * tol)

tol =  1/ (10**6)
a = 2
b = 4
print(secant(f, a, b, tol))
print(bisection(f, a, b, tol))
print(newton(f, df, a, tol))
	

