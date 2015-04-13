###Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.

class UndirectedGraphNodes:
	def __int__(self,x):
		self.label = x
		self.neighbours = []

def CloneGraph(node):
	def dfs(input,map):
		if input in map:
			return map[input]
		output = UndirectedGraphNodes(input.label)
		map[input]=output
		for neighbour in input.neighbours:
			output.neighbours.append(defs(neighbour,map))
		return output
	if node == None:
		return None
	return dfs(node,{})
