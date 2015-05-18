# Time:  O(n)
# Space: O(1)
#
# Given n non-negative integers a1, a2, ..., an, 
# where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of 
# line i is at (i, ai) and (i, 0). Find two lines, 
# which together with x-axis forms a container, 
# such that the container contains the most water.
# 
# Note: You may not slant the container.
#
class Solution:

	def containmostwater(array):
		if len(array) <= 1:
			return False
		elif len(array) == 2:
			return min(array)
		else:
			begin,end = 0,len(array)-1
			area = 0
			while begin < end:
				area = max(area,min(array[begin],array[end])*(end-begin))
				if array[begin] < array[end]:
					begin += 1
				else:
					end -= 1
			return area

if __name__ == "__main__":
    height = [1, 2, 3, 4, 3, 2, 1, 5]
    result = Solution().maxArea(height)
    print result
