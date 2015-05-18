###Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

###For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
###the contiguous subarray [4,−1,2,1] has the largest sum = 6.

#time O(n)
#space O(1)

class Solution:
	def maximumsubarray(self,A):
		maxsum = -100000
		curr = 0
		for i in range(1,len(A)):
			if curr < 0:
				curr = 0
			curr += A[i]
			maxsum = max(maxsum,curr)
		return maxsum
			
