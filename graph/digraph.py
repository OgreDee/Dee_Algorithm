#--encoding:utf-8--
#有向图
from queue import Queue
from bag import Bag
from graph_visualized import TreeVisualized 

class Digraph(object):
	#顶点数量
	num_vertexCnt = 0
	#边的数量
	num_edgeCnt = 0
	#邻接表
	arr_adj = None 

	def __init__(self, intext=None, vCnt=None):
		super(Digraph, self).__init__()

		if intext == None:
			self.num_vertexCnt = vCnt
			self.num_edgeCnt = 0
			self.arr_adj = [Bag() for i in range(self.num_vertexCnt)]
		else:
			lines = intext.split('\n')
			vertexCnt = int(lines[0])
			self.num_vertexCnt = vertexCnt
			self.num_edgeCnt = 0
			self.arr_adj = [Bag() for i in range(self.num_vertexCnt)]
			for x in range(1,len(lines)):
				vs = lines[x].split('-')
				self.AddEdge(int(vs[0]), int(vs[1]))


	def AddEdge(self, v, w):
		self.arr_adj[v].Add(w)
		self.num_edgeCnt = self.num_edgeCnt + 1

	def Reverse(self):
		disgraph = Digraph(vCnt = self.num_vertexCnt)
		for v in range(0, self.num_vertexCnt):
			for w in self.arr_adj[v]:
			 	disgraph.AddEdge(w.value, v)
		return disgraph

	def adj(self, v):
		return self.arr_adj[v]

	def V(self):
		return self.num_vertexCnt

	def E(self):
		return self.num_edgeCnt

	def Printf(self, fileName):
		TreeVisualized(True).printf(self, fileName)





class DigraphSearch(object):
	graph = None
	marked = None
	def __init__(self, digraph):
		super(DigraphSearch, self).__init__()
		self.graph = digraph
		self.marked = [False for i in range(digraph.V())]

	def beMarked(self, v):
		return self.marked[v] or False

	def mark(self, v):
		self.marked[v] = True

class DigraphDFS(DigraphSearch):
	def __init__(self, digraph, s):
		super(DigraphDFS, self).__init__(digraph, s)
		self.dfs(s)
	
	def dfs(self, v):
		print(v)
		self.mark(v)
		for next in self.graph.adj(v):
			if not self.beMarked(next.value):
				self.dfs(next.value)
		pass
		

class DirectedCycle(DigraphSearch):
	#是有向无环图
	beDAG = False

	def __init__(self, digraph):
		super(DirectedCycle, self).__init__(digraph)
		self.beDAG = True
		for x in range(0,self.graph.V()):
			if not self.beMarked(x):
				self.dfs_stack(x)

	#栈式(绳子算法)
	def dfs_stack(self, v):
		stack = []
		stack.append(v)
		# print(v)
		self.marked[v] = True
		while len(stack) > 0:
			stackTop = stack[len(stack)-1]

			for node in self.graph.arr_adj[stackTop]:
				if node.value in stack:
					stack.append(node.value)
					print("find cycle")
					print("stack: "+ ','.join([str(x) for x in stack]))
					stack.clear()
					self.beDAG = False
					return

				stack.append(node.value)

				if self.beMarked(node.value):
					stack.pop()
				else:
					self.marked[node.value] = True
					# print(node.value)
					stack.append(node.value)
					break
			stack.pop()

	def isDAG(self):
		return self.beDAG

		
class DepthFirstOrder(DigraphSearch):
	#前序排列
	pre = None
	#后序排列
	post = None
	#逆后序排列
	reversePost = None

	def __init__(self, digraph):
		super(DepthFirstOrder, self).__init__(digraph)
		self.reversePost = []
		self.pre = Queue()
		self.post = Queue()
		for x in range(0, digraph.V()):
			if not self.beMarked(x):
				self.dfs_recursion(x)
			pass
		self.reversePost.reverse()
		# print("Pre: " + str(self.pre.queue))
		# print("Post: " + str(self.post.queue))
		# print("ReversePost: " + str(self.reversePost))

	#递归式
	def dfs_recursion(self, v):
		self.pre.put(v)
		self.marked[v] = True
		for node in self.graph.arr_adj[v]:
			if not self.beMarked(node.value):
				self.dfs_recursion(node.value)
		self.post.put(v)
		self.reversePost.append(v)


#拓扑排序必须先检查是不是DAG(有向无环图)，然后再进行逆后续排序
class Topologicl(object):
	#顶点的拓扑顺序
	order = None
	def __init__(self, digraph):
		super(Topologicl, self).__init__()
		cycle = DirectedCycle(digraph)
		if cycle.isDAG():
			orderHelper = DepthFirstOrder(digraph)
			self.order = orderHelper.reversePost
	
	def Order(self):
		return self.order

	def IsDAG(self):
		return self.order != None


#---------------------------Test--------------------------------
str_graph = "6\n\
0-1\n\
0-5\n\
0-2\n\
1-2\n\
2-4\n\
2-3\n\
3-4\n\
3-0\n\
3-5"

str_graph_order="13\n\
0-6\n\
0-1\n\
0-5\n\
6-9\n\
9-10\n\
9-12\n\
9-11\n\
11-12\n\
2-0\n\
2-3\n\
3-5\n\
8-7\n\
7-6\n\
5-4\n\
6-4"

def main():
	# digraph = Digraph(str_graph)
	# digraph.Printf("digraph_default")
	# dfs = DigraphDFS(digraph, 0)
	# cycle = DirectedCycle(digraph, 5)
	# print("DAG: "+ str(cycle.isDAG()))

	digraphOrder = Digraph(str_graph_order)
	order = DepthFirstOrder(digraphOrder)
	digraphOrder.Printf("digraph_order")
	topologicl = Topologicl(digraphOrder)
	print("topologicl: " + str(topologicl.Order()))

	pass

if __name__ == '__main__':
	main()