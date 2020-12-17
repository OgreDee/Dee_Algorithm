#--encoding:utf-8--

class Node(object):
	value = None
	next = None

	def __init__(self, value):
		super(Node, self).__init__()
		self.value = value



class Bag(object):
	first = None
	count = 0

	def __init__(self):
		super(Bag, self).__init__()
	
	def Add(self, value):
		old = self.first
		self.first = Node(value)
		self.first.next = old
		self.count = self.count + 1
		return self.first

	def __iter__(self):
		self.node = self.first
		return self

	def __next__(self):
		while self.node != None:
			ret = self.node
			self.node = self.node.next
			return ret
		raise StopIteration()