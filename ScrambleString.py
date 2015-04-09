###https://oj.leetcode.com/problems/scramble-string/

def isScramble(a,b):
	if len(a) != len(b):
		return False
	if a == b:
		return True
	alist = list(a)
	blist = list(b)
	alist.sort()
	blist.sort()
	if alist != blist:
		return False
	for i in range(1,len(a)):
		if isScramble(a[:i],b[:i]) and isScramble(a[i:],b[i:]):
			return True
		if isScramble(a[:i],b[len(a)-i:]) and \
		   isScramble(a[i:],b[:len(a)-i]):
			return True
	return False
