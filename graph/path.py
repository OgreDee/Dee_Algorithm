from graph import Graph 

str_graph = "6\n\
8\n\
0-1\n\
0-5\n\
0-2\n\
1-2\n\
2-4\n\
2-3\n\
3-4\n\
3-5"



#深度优先遍历
#路径使用Tremaux算法: 把第一次到达的点的路径记录下来
class DepthFirstPaths(object):
	graph = None
	s = 0
	marked = None
	edgeTo = None
	def __init__(self, graph, s):
		super(DepthFirstPaths, self).__init__()
		self.graph = graph
		self.s = s
		self.marked = [False for i in range(graph.V())]
		self.edgeTo = [-1 for i in range(graph.V())]
		self.dfs(self.s)


	#深度优先遍历
	def dfs(self, v):
		self.marked[v] = True
		for next in self.graph.arr_adj[v]:
			if not self.beMarked(next.value):
				print(next.value, "---->", v)
				self.edgeTo[next.value] = v
				self.dfs(next.value)

	def beMarked(self, v):
		return self.marked[v] or False
		

	def pathTo(self, v):
		l = []
		p = v
		while p != self.s and p > -1:
			l.append(p)
			p = self.edgeTo[p]
		
		if p == self.s:
			l.append(self.s)
			l.reverse()
		else:
			l.clear()
		print("->".join([str(x) for x in l]))

def main():
	graph = Graph(str_graph)
	graph.Printf("default")
	search = DepthFirstPaths(graph, 5)
	search.pathTo(2)

if __name__ == '__main__':
	main()