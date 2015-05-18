###Given n non-negative integers representing an elevation map where the width of each bar is 1, 
###compute how much water it is able to trap after raining.
# time O(n)
#space O(n)

    def trap(A):
        leftmosthigh = [0]*len(A)
        leftmax = 0
        for i in range(len(A)):
            if A[i] > leftmax: 
              leftmax = A[i]
            leftmosthigh[i] = leftmax
        sum = 0
        rightmax = 0
        for i in range(len(A)-1:-1:-1):
            if A[i] > rightmax: 
              rightmax = A[i]
            if min(rightmax, leftmosthigh[i]) > A[i]:
                sum += min(rightmax, leftmosthigh[i]) - A[i]
        return sum

# Time:  O(n)
# Space: O(n)
class Solution2:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        stack = []
        
        for i in xrange(len(A)):
            mid_height = 0
            while stack:
                [pos, height] = stack.pop()
                result += (min(height, A[i]) - mid_height) * (i - pos - 1)
                mid_height = height
                
                if A[i] < height:
                    stack.append([pos, height])
                    break
            stack.append([i, A[i]])
            
        return result

#time O(n)
#space O(1)

class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        result = 0
        top = 0
        for i in xrange(len(A)):
            if A[top] < A[i]:
                top = i
        
        second_top = 0
        for i in xrange(top):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
            
        second_top = len(A) - 1
        for i in reversed(xrange(top, len(A))):
            if A[second_top] < A[i]:
                second_top = i
            result += A[second_top] - A[i]
            
        return result    
if __name__ == "__main__":
    print Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
