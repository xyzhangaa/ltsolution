###Given two strings s and t, determine if they are isomorphic.

###Two strings are isomorphic if the characters in s can be replaced to get t.

###All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

class Solution:
  def isIsomorphicStrs(self,s,t):
    if len(s) != len(t):
      return False
    s_dict={};t_dict={}
    for i in range(len(s)):
      if s[i] in s_dict.keys() and s_dict[s[i]] != t[i]:
        return False
      if t[i] in t_dict.keys() and t_dict[t[i]] != s[i]:
        return False
      s_dict[s[i]] = t[i]
      t_dict[t[i]] = s[i]
    return True
