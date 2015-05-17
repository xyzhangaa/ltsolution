###Compare two version numbers version1 and version2.
###If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

###You may assume that the version strings are non-empty and contain only digits and the . character.
###The . character does not represent a decimal point and is used to separate number sequences.
###For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

###Here is an example of version numbers ordering:

###0.1 < 1.1 < 1.2 < 13.37

class Solution:
  def compareversionum(self,v1,v2):
    v1Arr = v1.split('.')
    v2Arr= v2.split('.')
    len1 = len(v1Arr)
    len2 = len(v2Arr)
    lenmax = max(len1,len2)
    for x in range(lenmax):
      v1token = 0
      if x < len1:
        v1token = int(v1Arr[x])
      v2token = 0
      if x < len2:
        v2token = int(v2Arr[x])
      if v1token < v2token:
        return -1
      if v1token > v2token:
        return 1
    return 0
