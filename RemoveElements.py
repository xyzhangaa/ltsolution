###Given an array and a value, remove all instances of that value in place and return the new length.
###The order of elements can be changed. It doesn't matter what you leave beyond the new length.
#time O(n)
#space O(1)

def RemoveElem(nums,elem):
  front,back = 0,0
  while front < len(nums):
    if nums[front] != elem:
      nums[back] = nums[front]
      back += 1
    front += 1
  return back

if __name__ == "__main__":
    print Solution().removeDuplicates([1, 1, 2])
