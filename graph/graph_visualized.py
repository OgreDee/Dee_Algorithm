#--encoding:utf-8--
#安装 Graphviz 2.38    https://blog.csdn.net/qq_44727566/article/details/108713682
#安装pygraphviz
import pygraphviz as pgv


class TreeVisualized():
	G = None
	style="filled"
	shape="ellipse"
	color="#B4E7B7"
	color_black="#000000"
	color_gray="#999999"
	directed = False

	def __init__(self, directed=False):
		super(TreeVisualized, self).__init__()
		self.directed = directed

	def addNodes(self, count):
		for x in range(0,count):
			self.G.add_node(str(x), style=self.style, shape=self.shape, color=self.color)

	def addEdges(self, list):
		for idx in range(0, len(list)):
			for item in list[idx]:
				self.G.add_edge(str(idx), str(item.value), color="#B4DBFF", penwidth=1.5)


	def printf(self, graph, fileName):
		if fileName == None:
			return

		self.G = pgv.AGraph(directed=self.directed, rankdir="TB")

		self.addNodes(graph.V())	
		self.addEdges(graph.arr_adj)	

		# 导出图形
		self.G.layout()
		self.G.draw(fileName + ".png", prog="dot")
		pass

class MSTVisualized():
	G = None
	style="filled"
	shape="ellipse"
	color="#B4E7B7"
	color_black="#000000"
	color_gray="#999999"
	directed = False

	def __init__(self, directed=False):
		super(MSTVisualized, self).__init__()
		self.directed = directed

	def addNodes(self, count):
		for x in range(0,count):
			self.G.add_node(str(x), style=self.style, shape=self.shape, color=self.color)

	def addEdges(self, list):
		for idx in range(0, len(list)):
			for edge in list[idx]:
				v = edge.value.either()
				w = edge.value.other(v)
				self.G.add_edge(str(v), str(w), color="#B4DBFF", penwidth=1.5)


	def printf(self, graph, fileName):
		if fileName == None:
			return

		self.G = pgv.AGraph(directed=False, rankdir="TB")

		self.addNodes(graph.V())	
		self.addEdges(graph.arr_adj)	

		# 导出图形
		self.G.layout()
		self.G.draw(fileName + ".png", prog="dot")
		pass
