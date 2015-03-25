###Given an input string, reverse the string word by word.

def reversestring(string):
	A = string.split()
	newstring = ''
	for i in range(len(A)-1,0,-1):
		newstring += A[i]+' '
	newstring += A[0]
	return newstring
