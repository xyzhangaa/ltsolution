###All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

###Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

class Solution:
    # @param {string} s
    # @return {string[]}
    def findRepeatedDnaSequences(self, s):
        res = []
        htable = {}
        for i in range(len(s)-9):
            sub = s[i:i+10]
            if sub in htable:
                htable[sub] += 1
            else:
                htable[sub] = 1
        for item in htable:
            if htable[item] >= 2:
                res.append(item)
        return res
