###Given n non-negative integers representing an elevation map where the width of each bar is 1, 
###compute how much water it is able to trap after raining.

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
