###Implement wildcard pattern matching with support for '?' and '*'.

###'?' Matches any single character.
###'*' Matches any sequence of characters (including the empty sequence).

###The matching should cover the entire input string (not partial).

###The function prototype should be:
###bool isMatch(const char *s, const char *p)

###Some examples:
###isMatch("aa","a") → false
###isMatch("aa","aa") → true
###isMatch("aaa","aa") → false
###isMatch("aa", "*") → true
###isMatch("aa", "a*") → true
###isMatch("ab", "?*") → true
###isMatch("aab", "c*a*b") → false

###Analysis:

###For each element in s
###If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
###If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
###If not match, then we check if there is a * previously showed up,
###       if there is no *,  return false;
###       if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

###e.g.

###abed
###?b*d**

###a=?, go on, b=b, go on,
###e=*, save * position star=3, save s position ss = 3, p++
###e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
###d=d, go on, meet the end.
###check the rest element in p, if all are *, true, else false;

###Note that in char array, the last is NOT NULL, to check the end, use  "*p"  or "*p=='\0'".
#time O(m+n)
#space O(1)
def wildmatching(s,t):
	i = 0
	j = 0
	pos = -1
	ss = 0
	while i < len(s):
		if j < len(t) and (s[i] == t[j] or t[j] == '?'):
			i += 1
			j += 1
			continue
		if j < len(t) and t[j] == '*':
			pos = j
			j += 1
			ss = i
			continue
		if pos != -1:
			j = pos+1
			ss += 1
			i = ss
			continue
		return False
	while j < len(t) and t[j] == '*':
		j+= 1
	if j == len(t):
		return True
	return False
