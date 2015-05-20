# Time:  O(n)
# Space: O(1)
#
# Given an unsorted integer array, find the first missing positive integer.
# 
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
# 
# Your algorithm should run in O(n) time and uses constant space.
#

###swap

def firstmissingpos(A):
	i = 0
	while i <= len(A)-1:
		if i+1 == A[i]:
			i+= 1
		elif A[i] <= 0:
			i+=1
		elif A[i] > len(A):
			i+=1
		elif A[i] == A[A[i]-1]:
			i+=1
		else:
			tmpa,tmpb = i, A[i]-1
			A[tmpa],A[tmpb] = A[tmpb],A[tmpa]
	for i in range(len(A)):
		if i+1 != A[i]:
			return i+1
	return len(A)+1

class Solution2:
	def fistmissingpositive(self,nums):
		i = 0
		while i < len(nums):
			if nums[i] > 0 and nums[i]-1 < len(nums) and nums[i] != nums[nums[i]-1]:
				nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
			else:
				i += 1
		for i, integer in enumerate(nums):
			if i+1 != integer:
				return i+1
		return len(nums)+1


if __name__ == "__main__":
    print Solution().firstMissingPositive([1,2,0])
    print Solution().firstMissingPositive([3,4,-1,1])
