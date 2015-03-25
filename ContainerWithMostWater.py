def containmostwater(array):
	if len(array) <= 1:
		return False
	elif len(array) == 2:
		return min(array)
	else:
		begin,end = 0,len(array)-1
		area = 0
		while begin < end:
			area = max(area,min(array[begin],array[end])*(end-begin))
			if array[begin] < array[end]:
				begin += 1
			else:
				end -= 1
		return area
