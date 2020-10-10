class TreeNode:
	lnode = None
	rnode = None
	parent = None
	value = None

	def __init__(self, value):
		self.value = value

	def SetLeftNode(node):
		self.lnode = node

	def SetRightNode(node):
		self.rnode = node

	def SetParent(node):
		self.parent = node
		pass

	def __str__(self):
		return str(self.value)


#二叉搜索树(BinarySearchTree)
#如果节点的左子树不空，则左子树上所有结点的值均小于等于它的根结点的值；
#如果节点的右子树不空，则右子树上所有结点的值均大于等于它的根结点的值；
#任意节点的左、右子树也分别为二叉搜索树；
class BST:
	root = None
	def __init__(self, root=None):
		self.root = root
		pass

	def AddNode(node):
		if node == None:
			return

		if self.root == None:
			self.root = node
		else:



	def Add(value):
		node = TreeNode(value)
		if self.root == None:
			self.root = node
		else:
