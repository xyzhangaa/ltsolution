def permutationseq(n,k):
	fac = 1
	for i in range(1,n):
		fac *= i
	k -= 1
	num = [1,2,3,4,5,6,7,8,9]
	result = ''
	for i in reversed(range(n)):
		current = num[int(k/fac)]
		num.remove(current)
		result += str(current)
		if i != 0:
			k = k%fac
			fac /= i
	return result
