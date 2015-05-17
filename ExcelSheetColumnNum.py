###Given a non-zero positive integer, return its corresponding column title as appear in an Excel sheet.

class Solution:
  def excelsheetcolumnnum(self,s):
    res = 0
    for char in s:
      res = res*26+(ord(char) - ord('A')+1)
    return res
