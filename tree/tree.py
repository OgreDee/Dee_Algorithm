class Node:
	key = None
	value = None
	lnode = None
	rnode = None
	parent = None
	size = 0

	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.size = 1

	def Size(self):
		return self.size 

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
#Put
#Get
#MaxKey/MinKey
#Min
#Select
#Rank
#Delete
#DeleteMin
class BST:
	root = None

	def __init__(self):
		pass

	def IsEmpty(self):
		return self.root != None		

	#插入
	def Put(self, key, value):
		self.root = self.put(self.root, key, value)
	
	#查找
	def Get(self, key):
		return self.get(self.root, key)

	#遍历
	def Traverse(self):
		self._traverse(self.root)

	#图形
	def Graphy(self):
		dict = {}
		self._graphy(dict, self.root, 0)
		print("-------------------------------Graphy-------------------------------")
		for floor in dict.keys():
			vfloor = dict[floor]
			keys = vfloor.keys()
			for key in keys:
				print(floor, ":", key)
				children = vfloor[key]
				for node in children:
					print("\tchild: ", node)

	#最大键
	def MaxKey(self):
		node = self.root
		while node.rnode != None:
			node = node.rnode
		return node and node.key or None

	#最小键
	def MinKey(self):
		node = self.root
		while node.lnode != None:
			node = node.lnode
		return node and node.key or None

	#子树的最小节点
	def Min(self, i_node):
		node = i_node
		while node.lnode != None:
			node = node.lnode
		return node 

	#选取排名的值
	def Select(self, rank):
		node = self._select(self.root, rank)
		return node != None and node.key or None

	#查找名次
	def Rank(self, key):
		return self._rank(self.root, key)


	#删除
	def Delete(self, key):
		self.root = self._delete(self.root, key)

	def DeleteMin(self):
		self.root = self._deleteMin(self.root)

	def _rank(self, node, key):
		if node == None:
			return 0

		if node.key > key:
			return self._rank(node.lnode, key)
		elif node.key < key:
			return self.size(node.lnode) + self._rank(node.rnode, key) + 1
		else:
			return self.size(node.lnode)
		

	def _select(self, node, rank):
		if node == None:
			return None

		count =  self.size(node.lnode)

		if count < rank:
			return self._select(node.rnode, rank - count - 1)
		elif count > rank:
			return self._select(node.lnode, rank)
		else:
			return node


	def put(self, node, key, value):
		if node == None:
			node = Node(key, value)
		else:
			if node.key > key:
				node.lnode = self.put(node.lnode, key, value)
			elif node.key < key:
				node.rnode = self.put(node.rnode, key, value)
			else:
				print("same key: ", key)
				node.value = value
			node.size = self.size(node.lnode) + self.size(node.rnode) + 1

		return node

	def get(self, node, key):
		if node == None:
			return None

		if node.key > key:
			return self.get(node.lnode, key)
		elif node.key < key:
			return self.get(node.rnode, key)
		else:
			print("find ", node.value)
			return node.value

	#中序遍历
	def _traverse(self, node):
		if node == None:
			return

		print(node.key, " > ", node.value)
		if node.lnode != None:
			self._traverse(node.lnode)
		
		if node.rnode != None:
			self._traverse(node.rnode)

	def _graphy(self, dict, node, floor):
		if node == None:
			return

		floorDict = dict.get(floor)
		if floorDict == None:
			floorDict = {}
			dict[floor] = floorDict

		children = floorDict.get(node.key)
		if children == None:
			children = []
			floorDict[node.key] = children

		if node.lnode != None:
			children.append(node.lnode.key)
			self._graphy(dict, node.lnode, floor + 1)

		if node.rnode != None:
			children.append(node.rnode.key)
			self._graphy(dict, node.rnode, floor + 1)

		pass

	def _deleteMin(self, node):
		if node.lnode == None:
			return node.rnode

		node.lnode = self._deleteMin(node.lnode)
		node.size = self.size(node.lnode) + self.size(node.rnode) + 1
		return node

	def _delete(self, node, key):
		if node == None:
			return None
		
		if key < node.key:
			#左子树遍历
			node.lnode = self._delete(node.lnode, key)
		elif key > node.key:
			#右子树遍历
			node.rnode = self._delete(node.rnode, key)
		else:
			if node.lnode == None:
				return node.rnode
			elif node.rnode == None:
				return node.lnode
			else:
				tmpNode = self.Min(node.rnode)
				tmpNode.rnode = self._deleteMin(node.rnode)
				tmpNode.lnode = node.lnode
			node = tmpNode

		node.size = self.size(node.lnode) + self.size(node.rnode) + 1
		return node


	def size(self, node):
		if node == None:
			return 0
		return node.Size()




print("---------------------二叉查找树(BinarySearchTree)---------------------")
tree = BST()
tree.Put("dee100", 100)
tree.Put("dee300", 300)
tree.Put("dee001", 1)
tree.Put("dee010", 10)
tree.Put("dee200", 200)
tree.Put("dee3001", 3001)


# print(":> Traverse")
# tree.Graphy()

print("\n:> MaxMinKey")
print("\tMinKey: ", tree.MinKey())
print("\tMaxKey: ", tree.MaxKey())

print("\n:> Get")
print("\tdee001: ", tree.Get("dee001"))

print("\n:> Select")
print("\trank=0 : ", tree.Select(0))
print("\trank=1 : ", tree.Select(1))
print("\trank=2 : ", tree.Select(2))
print("\trank=3 : ", tree.Select(3))
print("\trank=4 : ", tree.Select(4))
print("\trank=5 : ", tree.Select(5))

print("\n:> Rank")
print("\t dee001 rank=",  tree.Rank("dee001"))
print("\t dee010 rank=",  tree.Rank("dee010"))
print("\t dee200 rank=",  tree.Rank("dee200"))
print("\t dee300 rank=",  tree.Rank("dee300"))


# print("\n:> DeleteMin")
# tree.DeleteMin()
tree.Graphy()
print("\n:> Delete dee300")
tree.Delete("dee300")
tree.Graphy()
print("\n:> Delete dee001")
tree.Delete("dee001")
tree.Graphy()
