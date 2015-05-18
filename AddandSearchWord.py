# Time:  O(min(n, h)), per operation
# Space: O(min(n, h))
#
# Design a data structure that supports the following two operations:
#
# void addWord(word)
# bool search(word)
# search(word) can search a literal word or a regular expression string containing only letters a-z or .. 
# A . means it can represent any one letter.
#
# For example:
#
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true
# Note:
# You may assume that all words are consist of lowercase letters a-z.
#

class TrieNode:
  def __init__(self):
    self.flag = False
    self.childs = {}

class WordDict:
  def __init__(self):
    self.root = TrieNode()
# Add a word into the data structure
  def addWord(self,word):
    curr = self.root
    for c in word:
      if not c in curr.childs:
        curr.childs[c] = TrieNode()
      curr = curr.childs[c]
    curr.flag = True
# Return if the word is in the data structure. A word could contain the dot character to represent any char
  def search(self,word):
    return self.searchhelper(word,0,self.root)
  def searchhelper(self,word,start,curr):
    if start == len(word):
      return curr.flag
    if word[start] in curr.childs:
      return self.searchhelper(word,start+1,curr.childs[word[start]])
    elif word[start] == '.':
      for c in curr.childs:
        if self.searchhelper(word,start+1,curr.childs[c]):
          return True
    return False
  
