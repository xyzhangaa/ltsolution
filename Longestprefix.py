# Time:  O(n1 + n2 + ...)
# Space: O(1)
# Write a function to find the longest common prefix string amongst an array of strings.



def longestprefix(strs):
	longestpre = strs[0]
	for string in strs[1:]:
		i = 0
		while i < longestpre and i < len(string) \
		      and string[i] == strs[0][i]:
			i += 1
		longestpre = min(longestpre,i)
	return strs[0][:longestpre]

if __name__ == "__main__":
    print Solution().longestCommonPrefix(["hello", "heaven", "heavy"])
