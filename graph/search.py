from graph import Graph 
from queue import Queue

str_graph = "7\n\
9\n\
0-6\n\
0-1\n\
0-5\n\
0-2\n\
1-2\n\
2-4\n\
2-3\n\
3-4\n\
3-5"

str_graph_cc = "13\n\
13\n\
0-5\n\
0-1\n\
0-2\n\
0-6\n\
5-3\n\
5-4\n\
3-4\n\
4-6\n\
7-8\n\
9-10\n\
9-11\n\
9-12\n\
11-12"



class Search(object):
	graph = None
	s = 0
	marked = None
	def __init__(self, graph, s):
		super(Search, self).__init__()
		self.graph = graph
		self.s = s
		self.marked = [False for i in range(graph.V())]

	#深度优先遍历
	def dfs(self, v):
		print(v)
		self.marked[v] = True
		for next in self.graph.arr_adj[v]:
			if not self.beMarked(next.value):
				self.dfs(next.value)

	def beMarked(self, v):
		return self.marked[v] or False

	def mark(self, v):
		self.marked[v] = True
		

#深度优先遍历
#栈式和递归式		
class DFS(Search):
	#递归式
	def dfs_recursion(self, v):
		print(v)
		self.marked[v] = True
		for node in self.graph.arr_adj[v]:
			if not self.beMarked(node.value):
				self.dfs_recursion(node.value)
	
	#栈式(绳子算法)
	def dfs_stack(self, v):
		stack = []
		stack.append(v)
		print(v)
		self.marked[v] = True
		while len(stack) > 0:
			stackTop = stack[len(stack)-1]

			for node in self.graph.arr_adj[stackTop]:
				stack.append(node.value)
				
				if self.beMarked(node.value):
					stack.pop()
				else:
					# print(">> in : "+str(node.value))
					self.marked[node.value] = True
					print(node.value)
					stack.append(node.value)
					break
			stack.pop()

		


#广度优先遍历
class BFS(Search):
	edgeTo = None

	def __init__(self, graph, s):
		super(BFS, self).__init__(graph, s)
		self.edgeTo = [s for i in range(graph.V())]
		self.bfs(graph, s)

	def bfs(self, graph, s):
		queue = Queue()
		queue.put(s)
		self.mark(s)
		while not queue.empty():
			top = queue.get()
			for node in self.graph.arr_adj[top]:
				v = node.value
				if not self.beMarked(v):
					queue.put(v)
					self.edgeTo[v] = top
					self.mark(v)

	def path(self, v):
		l = []
		l.append(v)
		while v != self.s:
			l.append(self.edgeTo[v])
			v = self.edgeTo[v]
		l.reverse()
		print("->".join([str(x) for x in l]))
		

class ConnectedComponent(Search):
	#顶点对应的连通分量的id
	id = None
	#id计数
	idTime = 0
	def __init__(self, graph):
		super(ConnectedComponent, self).__init__(graph, 0)
		self.id = [0 for i in range(graph.V())]
		self.idTime = 0
		for v in range(1, graph.V()):
			if not self.beMarked(v):
				self.dfs_recursion(v)
				self.idTime = self.idTime + 1
		
	#递归式
	def dfs_recursion(self, v):
		# print(v)
		self.marked[v] = True
		self.id[v] = self.idTime
		# print(str(v)+ " : " + str(self.idTime))
		for node in self.graph.arr_adj[v]:
			if not self.beMarked(node.value):
				self.dfs_recursion(node.value)

	def beConnected(self, v, w):
		return self.ID(v) == self.ID(w)

	def ID(self, v):
		return self.id[v]

	def count(self):
		return self.idTime


def main():
	graph = Graph(str_graph)
	graph.Printf("default")

	print("dfs...........")
	search = DFS(graph, 0)
	search.dfs_stack(0)

	print("bfs...........")
	bfs = BFS(graph, 0)
	bfs.path(4)

	print("cc............")
	graphCC = Graph(str_graph_cc)
	cc = ConnectedComponent(graphCC)
	graphCC.Printf("graph_cc")
	print("cc count: "+str(cc.count()))
	print("4 connect 10: " + str(cc.beConnected(4, 10)))


if __name__ == '__main__':
	main()