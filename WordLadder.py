###Given two words (start and end), and a dictionary, find the length of shortest transformation 
###sequence from start to end, such that:

###Only one letter can be changed at a time
###Each intermediate word must exist in the dictionary
###For example,

###Given:
###start = "hit"
###end = "cog"
###dict = ["hot","dot","dog","lot","log"]

###As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
###return its length 5.

###Note:

###Return 0 if there is no such transformation sequence.
###All words have the same length.
###All words contain only lowercase alphabetic characters.

def WordLadder(start,end,diction):
	diction.append(end)
	q = []
	q.append((start,1))
	while q:
		curr = q.pop(0)
		currword = curr[0]
		count = curr[1]
		if currword == end:
			return count
		for item in diction:
			nondup = 0
			for i in range(len(currword)):
				if item[i] != currword[i]:
					nondup += 1
			if nondup == 1:
				q.append((item,count+1))
				diction.remove(item)
	return 0
