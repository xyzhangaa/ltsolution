def lonsubnodup(string):
	begin,end=0,1
	maxlen = 0
	temp = string[begin:end+1]
	while end < len(string):
		if string[end] in temp:
			index = temp.index(string[end])
			maxlen = max(maxlen, len(temp))
			tempsub = temp[index:len(temp)-1]
			temp = tempsub+string[end]
		else:
			end += 1
	if end == len(string)-1:
		maxlen=max(maxlen,temp)
	return maxlen
