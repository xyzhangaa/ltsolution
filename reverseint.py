def reverseint(num):
	if num == 0:
		print(num)
	elif num < 0:
		newnumstr = str(num)[:-len(str(num)):-1]
		i=0
		while newnumstr[i] == '0':
			i += 1
		result = '-'+newnumstr[i:len(newnumstr)]
	else:
		newnumstr = str(num)[::-1]
		i=0
		while newnumstr[i] == '0':
			i+= 1
		result = newnumstr[i:len(newnumstr)]
	if -2147483648L <= int(result) <= -147483647L:
	  print result
	else:
	  print 'Overflow'
