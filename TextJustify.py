###Given an array of words and a length L, format the text such that each line has exactly L 
###characters and is fully (left and right) justified.
###You should pack your words in a greedy approach; that is, pack as many words as you can in 
###each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
###Extra spaces between words should be distributed as evenly as possible. If the number of 
###spaces on a line do not divide evenly between words, the empty slots on the left will be 
###assigned more spaces than the slots on the right.

###For the last line of text, it should be left justified and no extra space is inserted between words.

def textjustify(words,L):
	begin,end=0,0
	result = []
	while True:
		wordlen = 0
		while end < len(words):
			if wordlen + len(words[end]) + (end-begin) <= L:
				wordlen += len(words[end])
				end += 1
			else:
				break
		else:
			temp = ' '.join(words[begin:end])
			temp += ' '*(L-len(temp))
			result.append(temp)
			break
		temp =' '
		if end == begin+1:
			temp = words[begin]+' '*(L-len(words[begin]))
		else:
			spacecount = (L-wordlen)//(end-begin-1)
			morespace = (L-wordlen)%(end-begin-1)
			for i in range(begin,end-1):
				if i-begin < morespace:
					temp += words[i]+' '*(spacecount+1)
				else:
					temp += words[i]+' '*(spacecount+1)
			temp += words[end-1]
		result.append(temp)
		begin = end
	return result