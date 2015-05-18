# Time:  O(n), per operation
# Space: O(1)

#Implement a trie with insert, search, and startsWith methods.

#Note:You may assume that all inputs are consist of lowercase letters a-z.

# Initialize your data structure here
class TrieNode:
  def __init__(self):
    self.childs = dict{}
    self.isWord = False

class Trie:
  def __init__(self):
    self.root= TrieNode()
    
    # Inserts a word into the trie
  def insert(self,word):
    node = self.root
    for letter in word:
      child = node.childs.get(letter)
      if child is None:
        child = TrieNode()
        node.childs[letter] = child
      node = child
    node.isWord = True
  
  # Return if the word is in the trie
  def search(self,word):
    node=self.root
    for letter in word:
      node = node.childs.get(letter)
      if node is None:
        return False
    return node.isWord
  
  #Return if there is any word in the trie that starts with the given prefix
  def startwith(self,prefix):
    node= self.root
    for letter in prefix:
      node= node.childs.get(letter)
      if node is None:
        return False
    return True
  
  
