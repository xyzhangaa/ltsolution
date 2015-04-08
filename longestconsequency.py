###Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

###For example,
###Given [100, 4, 200, 1, 3, 2],
###The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
###Your algorithm should run in O(n) complexity.


### Hash Table
def longestconseq(A):
	dict = {x : False for x in A}
	maxlen = -1
	for i in dict:
		if dict[i] == False:
			curr = i+1
			lenright = 0
			while curr in dict:
				lenright += 1
				dict[curr] = True
				curr += 1
			curr = i-1
			lenleft = 0
			while curr in dict:
				lenleft += 1
				dict[curr]= True
				curr -= 1
		maxlen = max(maxlen,lenleft+lenright+1)
	return maxlen
	
	### sort and search
	    def longestConsecutive(num):
        # Key (begin, exclusive) => Value (end, inclusive)
        segments = {}
        # Key (end, exclusive) => Value (begin, inclusive)
        reversedSegments = {}
        
        for item in set(num):
            if item in segments and item in reversedSegments:
                # This item could connect two segments.
                newEnd = segments[item]
                del segments[item]
                
                newBegin = reversedSegments[item]
                del reversedSegments[item]
                
                segments[newBegin-1] = newEnd
                reversedSegments[newEnd+1] = newBegin
            elif item in segments:
                # This item could extend one segment's beginning.
                oldEnd = segments[item]
                del segments[item]
                
                segments[item-1] = oldEnd
                reversedSegments[oldEnd+1] = item
            elif item in reversedSegments:
                # This item could extend one segment's end.
                oldBegin = reversedSegments[item]
                del reversedSegments[item]
                
                segments[oldBegin-1] = item
                reversedSegments[item+1] = oldBegin
            else:
                # No adjacent segment. This item will create a new segment.
                segments[item-1] = item
                reversedSegments[item+1] = item
 
        # Find the length of the longest segment.
        maxLen = 0
        for segmentBegin in segments:
            segmentEnd = segments[segmentBegin]
            maxLen = max(maxLen, segmentEnd- segmentBegin)
        
        return maxLen
