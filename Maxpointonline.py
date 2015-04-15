###Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

def maxpointonline(points):
	if len(points) < 3:
		return len(points)
	result  = -1
	for i in range(len(points)):
		slope = {'inf' : 0}
		samepoint = 1
		for j in range(len(points)):
			if i == j:
				continue
			elif points[i][0] == points[j][0] and points[i][1] != points[j][1]:
				slope['inf'] += 1
			elif points[i][0] != points[j][0]:
				k = 1.0 * (points[i][1] - points[j][1])/(points[i][0]-points[j][0])
				if k not in slope:
					slope[k] = 1
				else:
					slope[k] += 1
			else:
				samepoint += 1
		result = max(result, max(slope.values())+samepoint)
	return result
