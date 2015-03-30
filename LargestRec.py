###Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.


def largestRecinHist(height):
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
	
def largestRec(matrix):
  if matrix == []:
    return 0
  a = [0 for i in range(len(matrix[0])]
  maxArea = 0
  for i in range(len(matrix)):
    for j in range(len(matrix[0])):
      if matrix[i][j] == 1:
        a[j] += 1
      else:
        a[j] = 0
    maxArea = max(maxArea, largestRecinHist(a))
  return maxArea
