# Time:  O(n)
# Space: O(n)
#
# Given an unsorted array, find the maximum difference between 
# 
# the successive elements in its sorted form.
# 
# Try to solve it in linear time/space.
# 
# Return 0 if the array contains less than 2 elements.
# 
# You may assume all elements in the array are non-negative integers
# 
#  and fit in the 32-bit signed integer range.

# radix sort/bucket sort
class Solution:
  def maximumgap(self,num):
    N = len(num)
    if N <2:
      return 0
    A = min(num)
    B = max(num)
    bucketRange = max(1,int((B-A-1)/(N-1))+1)
    bucketlen = (B-A)/bucketRange+1
    buckets= [None] * bucketlen
    for K in num:
      loc = (K-A)/bucketRange
      bucket = buckets[loc]
      if bucket is None:
        bucket = {'min':K,'max':K}
        buckets[loc] = bucket
      else:
        bucket['min']=min(bucket['min'],K)
        bucket['max'] = max(bucket['max'],K)
    maxgap = 0
    for x in range(bucketlen):
      if buckets[x] is None:
        continue
      y = x+1
      while y < bucketlen and buckets[y] is None:
        y+=1
      if y < bucketlen:
        maxgap = max(maxgap,buckets[y]['min']-buckets[x]['max'])
      x = y
    return maxgap

# bucket sort(considering duplicates)
class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
        
        unique_num = self.removeDuplicate(num)
        
        max_val, min_val = max(unique_num), min(unique_num)
        gap = (max_val - min_val) / (len(unique_num) - 1)
        bucket_size = (max_val - min_val) / gap + 1
        max_bucket = [float("-inf") for _ in xrange(bucket_size)]
        min_bucket = [float("inf") for _ in xrange(bucket_size)]

        for i in unique_num:
            if i in (max_val, min_val):
                continue      
            idx = (i - min_val) / gap
            max_bucket[idx] = max(max_bucket[idx], i)
            min_bucket[idx] = min(min_bucket[idx], i)
        
        max_gap = 0
        pre = min_val
        for i in xrange(bucket_size):
            if max_bucket[i] == float("-inf") and min_bucket[i] == float("inf"):
                continue
            max_gap = max(max_gap, min_bucket[i] - pre)
            pre = max_bucket[i]
        max_gap = max(max_gap, max_val - pre)
        
        return max_gap
    
    def removeDuplicate(self, num):
        dict = {}
        unique_num = []
        for i in num:
            if i not in dict:
                unique_num.append(i)
                dict[i] = True
        return unique_num

# Time:  O(nlogn)
# Space: O(n)
class Solution2:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        if len(num) < 2:
            return 0
            
        num.sort()
        pre = num[0]
        max_gap = float("-inf")
        
        for i in num:
            max_gap = max(max_gap, i - pre)
            pre = i
        return max_gap
     
if __name__ == "__main__":
    print Solution().maximumGap([3, 1, 1, 1, 5, 5, 5, 5])
