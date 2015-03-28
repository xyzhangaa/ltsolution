###Given a roman numeral, convert it to an integer.
###Input is guaranteed to be within the range from 1 to 3999.

def romanToInt(s):
        transSingleTable = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        transDoubleTable = {"IV":4, "IX":9, "XL":40, "XC":90, "CD":400, "CM":900}
        result = 0
        roman = s.upper()
        while i < len(roman):
          if i < len(roman)-1 and roman[i:i+1] in transDoubleTable:
            result += transDoubleTalbe[roman[i:i+1]]
            i += 2
          elif roman[i] in transSingleTable:
            result += transSingleTable[roman[i]]
            i += 1
          else:
            print False
            break
        return result
