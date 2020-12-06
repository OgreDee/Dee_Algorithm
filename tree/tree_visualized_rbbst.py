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
	color_red="#FF0000"

	def GetColor(self, node):
		if node.color:
			return self.color_red
		else:
			return self.color_black

	def addNode(self, node):
		if node.lnode != None:
			self.G.add_node(node.lnode.key, style=self.style, shape=self.shape, color=self.color)
			self.G.add_edge(node.key, node.lnode.key, color=self.GetColor(node.lnode), penwidth=5)
			self.addNode(node.lnode)	
		elif node.rnode != None:
			nullName = str(node.key) +"L"
			self.G.add_node(nullName, style=self.style, shape=self.shape, color=self.color_black)
			self.G.add_edge(node.key, nullName, color=self.color_gray, penwidth=0.5)	
			

		if node.rnode != None:
			self.G.add_node(str(node.rnode.key), style=self.style, shape=self.shape, color=self.color)
			self.G.add_edge(str(node.key), str(node.rnode.key), color=self.GetColor(node.rnode), penwidth=5)
			self.addNode(node.rnode)
		elif node.lnode != None:
			nullName = str(node.key) +"R"
			self.G.add_node(nullName, style=self.style, shape=self.shape, color=self.color_black)
			self.G.add_edge(str(node.key),nullName, color=self.color_gray, penwidth=0.5)	


	def printf(self,treeRoot, fileName):
		if fileName == None:
			return

		self.G = pgv.AGraph(directed=True, rankdir="TB")
		self.G.add_node(str(treeRoot.key), style=self.style, shape=self.shape, color=self.color)

		self.addNode(treeRoot)	

		# 导出图形
		self.G.layout()
		self.G.draw(fileName + ".png", prog="dot")
		pass

