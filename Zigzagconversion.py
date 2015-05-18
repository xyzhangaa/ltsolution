##Write the code that will take a string and make this conversion given a number of rows
#time O(n)
#space O(1)

def zigzag(s,rows):
  assert rows > 0
  if rows == 1:
    return s
  temp = [[] for _ in range(rows)]
  position = 0
  direction = 1
  for char in s:
    temp[position].append(char)
    if position == 0:
      direction = 1
    elif position == rows-1:
      direction = -1
    position += direction
  return ''.join([''.join(row) for row in temp])

#time O(n)
#space O(1)
class Solution:
  def convert(self,s,nRows):
      step, zigzag = 2*nRows-2, ''
      if s == None or len(s) == 0 or nRows <= 0:
        return ''
      if nRows == 1:
        return s
      for i in xrange(nRows):
        for j in xrange(i,len(s),step):
          zigzag += s[j]
          if i >0 and i < nRows-1 and j+step-2*i < len(s):
            zigzag += s[j+step-2*i]
      return zigzag
      
  if __name__ == '__main__':
    print Solution().convert('PATSJDIJWIJEI',3)
