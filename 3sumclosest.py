# Time:  O(n^2)
# Space: O(1)
#
# Given an array S of n integers, 
# find three integers in S such that the sum is closest to a given number, target. 
# Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
#
# For example, given array S = {-1 2 1 -4}, and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#

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
