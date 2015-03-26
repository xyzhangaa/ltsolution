def longestprefix(strs):
	longestpre = strs[0]
	for string in strs[1:]:
		i = 0
		while i < longestpre and i < len(string) \
		      and string[i] == strs[0][i]:
			i += 1
		longestpre = min(longestpre,i)
	return strs[0][:longestpre]
