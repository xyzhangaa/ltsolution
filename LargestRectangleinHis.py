###Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
###find the area of largest rectangle in the histogram.

# O(n), O(n)
def largestRec(height):
	stack = []
	maxArea = 0
	height.append(-1)
	index = 0
	while index < len(height):
		if len(stack) == 0:
			stack.append(index)
			index += 1
		elif height[index] >= height[stack[-1]]:
			stack.append(index)
			index += 1
		else:
			preBasin = stack.pop()
			if len(stack) == 0:
				maxArea=max(maxArea,height[preBasin]*index)
			else:
				maxArea=max(maxArea,height[preBasin]*(index-stack[-1]-1))
	return maxArea
