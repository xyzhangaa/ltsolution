def lonsubnodup(string):
	end = 1
	temp = string[0]
	longstr = ''
	while end < len(string):
		if string[end] in temp:
			if len(longstr) < len(temp):
				longstr = temp
			tempsub = temp[temp.index(string[end])+1:len(temp)]
			temp = tempsub+string[end]
			end += 1
		else:
			temp += string[end]
			end += 1
	else:
		if len(longstr) < len(temp):
			longstr = temp
	return longstr
