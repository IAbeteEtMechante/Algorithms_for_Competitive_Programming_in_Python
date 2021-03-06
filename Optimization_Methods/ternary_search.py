"""
good explanation here:
https://cp-algorithms.com/num_methods/ternary_search.html
https://www.youtube.com/watch?v=7h86n97naH4
"""

def ternary_search_discrete(f, a, b):
	"""
	input: a function that decreases first and increases after
	(monotonic parts not are not necessarly strictly monotonic,
	but the way my algo deals with the plateaus is not totally
	satisfactory imo, so be careful)
	output: returns an interval of length 3(in the general case) 
	and that interval contains the minimum
	we have to stop when the search interval
	becomes smaller than 3 : we cannot find 4 integers in there anymore
	"""
	while (b - a) >= 3:
		alpha = 1/3
		c = (1-alpha) * a + alpha * b
		c = int(c)
		d  = alpha * a + (1 - alpha) * b
		d = int(d)
		fc = f(c)
		fd = f(d)
		counter = 0
		while fc == fd:
			if counter % 2 == 0:
				d += 1
			else:
				c -= 1
			counter += 1
			if d > b or c < a:
				return (a,b)

		if fc < fd:
			b = d
		else:
			a  = c

	return (a, b)

def ternary_search_not_discrete(f, a, b, tol, max_iter):
	"""
	we assume that f is stricly decreasing then strictly 
	increasing on [a,b]
	"""
	step = 0
	while step < max_iter and (b - a) >= tol:
		step += 1
		alpha = 1/3
		c = (1-alpha) * a + alpha * b
		d  = alpha * a + (1 - alpha) * b
		fc = f(c)
		fd = f(d)

		if fc < fd:
			b = d
		else:
			a  = c

	return a
#example:
#https://codeforces.com/contest/1354/problem/C2
