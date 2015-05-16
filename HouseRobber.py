###You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

###Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        odd,even = 0,0
        for i in range(len(nums)):
            if i%2 == 0:
                odd = max(odd+nums[i],even)
            else:
                even = max(even+nums[i],odd)
        return max(odd,even)
