# Time:  O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
# For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
# For "bbbbb" the longest substring is "b", with the length of 1.
#
class Solution:
  def lengthoflongestsubstr(self,s):
    longest, start, visited = 0,0,[False for _ in range(256)]
    for i, char in enumerate(s):
      if visited[ord(char)]:
        while char != s[start]:
          visited[ord(s[start])] = False
          start += 1
        start += 1
      else:
        visited[ord(char)] = True
      longest = max(longest,i-start+1)
    return longest

class Solution:
  def longsubnodup(self,s):
    longest, start, visited = 0,0,[-1 for _ in range(256)]
    for i in range(len(s)):
      if visited[ord(s[i])] != -1:
        while start <= visited[ord(s[i])]:
          visited[ord(s[i])] = -1
          start += 1
      longest = max(longest,i-start+1)
      visited[ord(s[i])] = i
    return longest
