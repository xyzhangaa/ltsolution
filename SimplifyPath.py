###Given an absolute path for a file (Unix-style), simplify it.

###For example,
###path = "/home/", => "/home"
###path = "/a/./b/../../c/", => "/c"

###Corner Cases:
###Did you consider the case where path = "/../"? In this case, you should return "/".
###Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/". 
######In this case, you should ignore redundant slashes and return "/home/foo".

###Python string manipulation
###Interatively
#time O(n)
#space O(1)
def SimplifyPath(s):
	s = s.split('/')
	curr = '/'
	for i in s:
		if i == '..':
			if curr != '/':
				curr = '/'.join(curr.split('/')[:-1])
				if curr == '':
					curr = '/'
		elif i != '.' and i !='':
			if curr != '/':
				curr += '/'+i
			else:
				curr += i
	return curr


###stack
#time O(n)
#space O(n)
### No string manipulation
def SimplifyPathTwo(s):
	stack = []
	i = 0
	result = ''
	while i < len(s):
		end = i+1
		while end < len(s) and s[end] != '/':
			end += 1
		sub = s[i+1:end]
		if len(sub) > 0:
			if sub == '..':
				if stack != []:
					stack.pop()
			elif sub != '.':
				stack.append(sub)
		i = end
	if stack == []:
		return '/'
	for i in stack:
		result += '/'+i
	return result
