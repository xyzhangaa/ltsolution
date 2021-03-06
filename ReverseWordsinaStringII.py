# Time: O(n)
# Space:O(1)
#
# Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
# 
# The input string does not contain leading or trailing spaces and the words are always separated by a single space.
# 
# For example,
# Given s = "the sky is blue",
# return "blue is sky the".
# 
# Could you do it in-place without allocating extra space?
#

class Solution:
  def reversewords(self,s):
    self.reverse(s,0,len(s)):
    i =0 
    for j in xrange(len(s)+1):
      if j == len(s) or s[j] == ' ':
        self.reverse(s,i,j)
        i = j+1
  
  def reverse(self,s,begin,end):
    for i in xrange((end-begin)/2):
      s[begin+i],s[end-1-i] = s[end-1-i],s[being+i]
      
if __name__ == '__main__':
  s=....
  Solution().reversewords(s)
  preint s
