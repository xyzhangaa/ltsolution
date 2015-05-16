###Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of 
###which the sum ≥ s. If there isn't one, return 0 instead.

###For example, given the array [2,3,1,2,4,3] and s = 7, the subarray [4,3] has the minimal length under the problem constraint.

### O(n)
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        if len(nums) == 0:
            return 0
        left = 0; right = 0; sum=0; minlen = len(nums)+1
        while right < len(nums):
            while sum < s and right < len(nums):
                sum += nums[right]
                right += 1
            while left < right and sum >= s:
                if sum >= s:
                    minlen = min(minlen,right-left)
                sum -= nums[left]
                left += 1
        if minlen > len(nums):
            return 0
        else:
            return minlen
            
### O(nlogn)
class Solution:
    # @param {integer} s
    # @param {integer[]} nums
    # @return {integer}
    def minSubArrayLen(self, s, nums):
        size = len(nums)
        left, right =0, size
        bestAns = 0
        while left <= right:
            mid = (left+right)/2
            if self.solve(mid,s,nums):
                bestAns = mid
                right = mid -1
            else:
                left = mid+1
        return bestAns
    def solve(self,l,s,nums):
        sums= 0
        for x in range(len(nums)):
            sums += nums[x]
            if x >= l:
                sums -= nums[x-l]
            if sums >= s:
                return True
        return False
