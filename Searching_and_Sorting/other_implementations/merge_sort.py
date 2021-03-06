from math import inf
from collections import deque

def merge(aa, bb):
	#needed otherwise deque(None) would return error
	if not aa:
		return bb
	if not bb:
		return aa

	qq1 = deque(aa)
	qq2 = deque(bb)
	result = []
	while qq1  and qq2:
		if qq1[0] <= qq2[0]:
			result.append(qq1.popleft())
		else:
			result.append(qq2.popleft())

	result += list(qq1)
	result += list(qq2)
	return result


def merge_sort(aa):
	n = len(aa)
	if n == 1:
		return aa
	return merge(merge_sort(aa[:n//2]), merge_sort(aa[n//2:]))


aa = [8,12,3,5,4,55,12,5,99,99,101,98,1,2,7,1,54,11]
print(aa)
print(merge_sort(aa))

