###Implement strStr().

###Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

### Brutal Force
# Time:  (n * m)
# Space: (1)

def strStr(haystack,needle):
	if len(haystack) < len(needle):
		return None
	i = 0
	while i < len(haystack)-len(needle)+1:
		j =0
		k = i
		while j < len(needle):
			if haystack[k] == needle[j]:
				j+=1
				k+=1
			else:
				break
		if j == len(needle):
			break
		else:
			i+=1
	if i == len(haystack)-len(needle)+1:
		return None
	else:
		return haystack[i]

### KMP
# Time:  O(n + m)
# Space: O(m)
def ComputePrefixFunction(needle):
	Pi = [0 for _ in range(len(needle))]
	m = len(needle)
	Pi[0] = 0
	k = 0
	for q in range(1,m):
		while k > 0 and needle[k] != needle[q]:
			k = Pi[k-1]
		if needle[k] == needle[q]:
			k += 1
		Pi[q] = k
	return Pi
	
def strStr(haystack,needle):
	n = len(haystack)
	m = len(needle)
	if m == 0:
		return haystack
	Pi = ComputePrefixFunction(needle)
	q = 0
	for i in range(n):
		while q > 0 and needle[q] != haystack[i]:
			q = Pi[q-1]
		if needle[q] == haystack[i]:
			q += 1
		if q ==m:
			return haystack[i-m+1:]
	return None
