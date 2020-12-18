#--encoding:utf-8--

from bag import Bag
from graph_visualized import TreeVisualized 


class Graph(object):
	#顶点数量
	num_vertexCnt = 0
	#边的数量
	num_edgeCnt = 0
	#邻接表
	arr_adj = None 

	def __init__(self, intext):
		super(Graph, self).__init__()

		lines = intext.split('\n')
		vertexCnt = int(lines[0])

		self.num_edgeCnt = int(lines[1])
		self.num_vertexCnt = vertexCnt
		self.arr_adj = [Bag() for i in range(vertexCnt)]
		for x in range(2,len(lines)):
			vs = lines[x].split('-')
			self.AddEdge(int(vs[0]), int(vs[1]))


	def AddEdge(self, v, w):
		self.arr_adj[v].Add(w)
		self.arr_adj[w].Add(v)

	def V(self):
		return self.num_vertexCnt

	def E(self):
		return self.num_edgeCnt

	def Printf(self, fileName):
		TreeVisualized(False).printf(self, fileName)

