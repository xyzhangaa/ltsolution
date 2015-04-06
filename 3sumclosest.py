def threesumclosest(num,target):
	num.sort()
	mindiff = 100000
	result = 0
	for i in range(len(num)):
		left = i+1
		right = len(num)-1
		while left < right:
			sum=num[i]+num[left]+num[right]
			diff = abs(sum-target)
			if diff < mindiff:
				mindiff = diff
				result = sum
			elif sum == target:
				return sum
			elif sum < target:
				left += 1
			else:
				right -= 1
	return result
