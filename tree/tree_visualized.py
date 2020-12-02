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

	def addNode(self, node):
		if node.lnode != None:
			self.G.add_node(str(node.lnode.value), style=self.style, shape=self.shape, color=self.color)
			self.G.add_edge(str(node.value), str(node.lnode.value), color="#B4DBFF", penwidth=1.5)
			self.addNode(node.lnode)	
		elif node.rnode != None:
			nullName = str(node.value) +"L"
			self.G.add_node(nullName, style=self.style, shape=self.shape, color=self.color_black)
			self.G.add_edge(str(node.value), nullName, color=self.color_gray, penwidth=0.5)	
			

		if node.rnode != None:
			self.G.add_node(str(node.rnode.value), style=self.style, shape=self.shape, color=self.color)
			self.G.add_edge(str(node.value), str(node.rnode.value), color="#B4DBFF", penwidth=1.5)
			self.addNode(node.rnode)
		elif node.lnode != None:
			nullName = str(node.value) +"R"
			self.G.add_node(nullName, style=self.style, shape=self.shape, color=self.color_black)
			self.G.add_edge(str(node.value),nullName, color=self.color_gray, penwidth=0.5)	


	def print(self,treeRoot, fileName):
		if fileName == None:
			return

		self.G = pgv.AGraph(directed=True, rankdir="TB")
		self.G.add_node(str(treeRoot.value), style=self.style, shape=self.shape, color=self.color)

		self.addNode(treeRoot)	

		# 导出图形
		self.G.layout()
		self.G.draw(fileName + ".png", prog="dot")
		pass

