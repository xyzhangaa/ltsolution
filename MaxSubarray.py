###Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

###For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
###the contiguous subarray [4,−1,2,1] has the largest sum = 6.




def MaxSubarray(nums):
	i = 0
	while nums[i] <= 0:
		i+=1
	maxsum =nums[i]
	total = nums[i]
	begin,end = i,i+1
	while i < len(nums):
		total += nums[i]
		if total <= 0:
			begin = i+1
			end = begin
			total = 0
		elif maxsum < total:
			maxsum = total
			end = i
		i += 1
	return begin,end,maxsum
