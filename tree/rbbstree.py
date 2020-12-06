#--encoding:utf-8--
#红黑二叉查找树
from tree_visualized_rbbst import TreeVisualized 


RED = True
BLACK = False

def formatInterge(num):
	return	'{:0>5d}'.format(num) 

class RBBSRNode:
	#是否是红色(到父节点的链接)
	color = BLACK
	key = None
	value = None

	lnode = None
	rnode = None

	def __init__(self, key, value, color):
		self.color = color
		self.key = key
		self.value = value



#红黑二叉查找树(对2-3-4树的实现)
#2-节点: 标准二叉树中的节点(一个键和两个链接的节点)
#3-节点: 两个键和三条链接
#2-3树: 可以含有2-或者3-节点
#红链接: 将两个2-节点连接构成一个3-节点
#黑链接: 2-3树中的普通节点
#空链接为黑链接
#颜色表示法: 节点的颜色是指指向自己的链接的颜色, 即父节点指向自己
#红黑树的定义:
# 	红色链接均为左链接
#	没有任何节点同时有红色左连接和红色右链接
#	树是完美黑色平衡的，即任意空链接到根节点的路径上的黑色链接数量相同(这个概念的理解需要把红色链接画平看)
#插入：
#  新插入的节点都是红链接
#  	2-节点插入新节点, 是右斜红链接需要左旋
#	3-节点插入新节点
#		(1)右插入, 改变颜色为黑 
#		(2)左插入，将上层的红链接右旋了，改变颜色为黑 
#		(3)中间插入, 红色左链接链接一条红色右链接, 将下层红链接左旋, 再重复二步骤
#	红色链接在树中向上传递,即左右都是红链接，中节点颜色修正为红flipColors
class RBBST:
	#根节点
	root = None
	visualizer = TreeVisualized()

	#图形
	def Graphy(self, outName):
		self.visualizer.printf(tree.root, outName)

	def Put(self, value):
		key = formatInterge(value) 
		self.root = self._put(self.root, key, value)
		self.root.color = BLACK

	def _isRed(self, node):
		if node == None:
			return BLACK
		return node.color == RED

	def _put(self, node, key, value):
		if node == None:
			return RBBSRNode(key, value, RED)
		else:
			if key < node.key: #往左节点插
				node.lnode = self._put(node.lnode, key, value)
			elif node.key < key: #往右节点插
				node.rnode = self._put(node.rnode, key, value)
			else:
				print("same key: ", key)
				node.value = value
				return
			
		if self._isRed(node.rnode) and not self._isRed(node.lnode):
			#右斜了,左旋转
			node = self._rotateLeft(node)
		if self._isRed(node.lnode) and self._isRed(node.lnode.lnode):
			#红色链接在一条线上
			node = self._rotateRight(node)
		
		if self._isRed(node.rnode) and self._isRed(node.lnode):
			self.flipColors(node)

		return node

	#左旋(把红色右斜链接转化为左链接)
	def _rotateLeft(self, node):
		rChild = node.rnode
		node.rnode = rChild.lnode
		rChild.lnode = node

		rChild.color = node.color
		node.color = RED
		
		return rChild

	#左旋(把红色左斜链接转化为右链接)
	def _rotateRight(self, node):
		lChild = node.lnode
		node.lnode = lChild.rnode
		lChild.rnode = node

		lChild.color = node.color
		node.color = RED

		return lChild

	def flipColors(self, node):
		node.lnode.color = BLACK
		node.rnode.color = BLACK
		node.color = RED


print("---------------------二叉查找树(BinarySearchTree)---------------------")
tree = RBBST()
# tree.Put('S', 1)
# tree.Put('E', 2)
# tree.Put('A', 4)
# tree.Put('R', 4)
# tree.Put('C', 4)
# tree.Put('H', 4)
# tree.Put('X', 4)
# tree.Put('M', 4)
# tree.Put('P', 4)
# tree.Put('L', 4)


tree.Put(1)
tree.Put(2)
tree.Put(3)
tree.Put(4)
tree.Put(5)
tree.Put(6)
tree.Put(7)
tree.Put(8)
tree.Put(9)
tree.Put(30)
tree.Put(1099)
tree.Put(3000)

tree.Graphy("root")