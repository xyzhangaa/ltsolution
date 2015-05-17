###Given a positive integer, return its corresponding column title as appear in an Excel sheet.

class Solution:
  def excelsheetcoltitle(self,num):
    res = ''
    while num:
      res = chr((num-1)%26+ord('A'))+res
      num = (num-1)/26
    return res
