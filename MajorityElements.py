###Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

###You may assume that the array is non-empty and the majority element always exist in the array.

###Hashtable Solution
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        if len(nums) == 0 :
            return None
        if len(nums) % 2 ==0:
            half = len(nums)/2
        else:
            half = len(nums)/2+1
        htable = {}
        for i in nums:
            if i in htable:
                htable[i] += 1
            else:
                htable[i] = 1
        for x in htable:
            if htable[x] >= half:
                return x
                
### Bit Manipulation
