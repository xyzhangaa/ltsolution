###You are given a string, S, and a list of words, L, that are all of the same length. 
###Find all starting indices of substring(s) in S that is a concatenation of each word in 
###L exactly once and without any intervening characters.

###For example, given:
###S: "barfoothefoobarman"
###L: ["foo", "bar"]

###You should return the indices: [0,9].
###(order does not matter).

def SubConcatenationWords(s,l):
	words = {}
	wordnum = len(l)
	for i in l:
		if i not in words:
			words[i] = 1
		else:
			words[i] += 1
	wordlen = len(l[0])
	result = []
	for i in range(len(s)+1-wordlen*wordnum):
		curr = {}
		j = 0
		while j < wordnum:
			word = s[i+j*wordlen:i+j*wordlen+wordlen]
			if word not in words:
				break
			if word not in curr:
				curr[word] = 1
			else:
				curr[word] + 1
			if curr[word] > words[word]:
				break
			j += 1
		if j == wordnum:
			result.append(i)
	return result
