# 树结构
#------------------------------嵌套列表实现树结构-----------------------------
# 标准索引访问列表子树。根节点tree[0],左子树tree[1],右子树tree[3]。子树同样为列表
def binaryTree(r):
	return [r,[],[]]

def insertLeft(root,newBranch):
	t = root.pop(1)
	if len(t) > 1:
		root.insert(1,[newBranch,t,[]])
	else:
		root.insert(1,[newBranch,[],[]])
	return root

def insertRight(root,newBranch):
	t = root.pop(2)
	if len(t) > 1:
		root.insert(2,[newBranch,t,[]])
	else:
		root.insert(2,[newBranch,[],[]])
	return root

def getRootValue(root):
	return root[0]

def setRootValue(root,newValue):
	root[0] = newValue

def getLeftChild(root):
	return root[1]

def getRightChild(root):
	return root[2]

#----------------------------“节点和引用”实现树结构--------------------
class binaryTree:
	"""docstring for binary"""
	def __init__(self,rootOB):
		self.key = rootOB
		self.leftchild = None
		self.rightchild = None

	def insertLeft(self,newNode):
		temp = binaryTree(newNode)
		if self.leftchild == None:
			self.leftchild = temp
		else:
			temp.leftchild, self.leftchild = self.leftchild, temp

	def insertRight(self,newNode):
		temp = binaryTree(newNode)
		if self.rightchild == None:
			self.rightchild = binaryTree(newNode)
		else:
			temp.rightchild,self.rightchild = self.rightchild,temp

	def getRightChild(self):
		return self.rightchild

	def getLeftChild(self):
		return self.leftchild

	def setRooTValue(self,obj):
		self.key = obj

	def getRootValue(self):
		return self.key

#---------------------------树结构实例-------------------------
#生成数学表达式解析树
def buildParseTree(fpexp):
	fplist = fpexp.split()
	pStack = Stack()
	eTree = binaryTree("")
	pStack.push(eTree)
	currentTree = eTree
	for i in fplist:
		if i == "(":
			currentTree.insertLeft("")
			pStack.push(currentTree)
			currentTree = currentTree.getLeftChild()
		elif i not in ["+","-","*","/",")"]:
			currentTree.setRooTValue(int(i))
			parent = pStack.pop()
			currentTree = parent
		elif i in ["+","-","*","/"]:
			currentTree.setRooTValue(i)
			currentTree.insertRight("")
			pStack.push(currentTree)
			print(type(currentTree))
			currentTree = currentTree.getRightChild()
		elif i == ")":
			parent = pStack.pop()
			currentTree = parent
		else:
			raise ValueError
	return eTree

#计算表达式
def evaluate(parseTree):
	opers = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}
	
	leftC = parseTree.getLeftChild()
	rightC = parseTree.getRightChild()

	if leftC and rightC:
		fn = opers[parseTree.getRootValue()]
		return fn(evaluate(leftC),evaluate(rightC))
	else:
		return parseTree.getRootValue()

#------------------------------树遍历-----------------------------------
#前序遍历
def preorder(tree):
	if tree:
		print(tree.getRootValue())
		preorder(tree.getLeftChild())
		preorder(tree.getRightChild())

#中序遍历
def inorder(tree):
	if tree:
		inorder(tree.getLeftChild())
		print(tree.getRootValue())
		inorder(tree.getRightChild())

#后序遍历
def postorder(tree):
	if tree != None:
		postorder(tree.getLeftChild())
		postorder(tree.getRightChild())
		print(tree.getRootValue())

#后序遍历表达式求值
def postordereval(tree):
	opers = {"+":operator.add,"-":operator.sub,"*":operator.mul,"/":operator.truediv}

	res1 = None
	res2 = None

	if tree:
		res1 = postordereval(tree.getLeftChild())
		res2 = postordereval(tree.getRightChild())

		if res1 and res2:
			return opers[tree.getRootValue()](res1,res2)
		else:
			return tree.getRootValue()

#中序遍历生成全括号中缀表达式
def printexp(tree):
	sVal = ""
	if tree:
		sVal = "(" + printexp(tree.getLeftChild())
		sVal = sVal + str(tree.getRootValue())
		sVal = sVal + printexp(tree.getRightChild()) + ")"
	return sVal

#----------------------二叉堆(完全二叉树)---------------------------
#最小堆 优先队列
class binHeap:
	"""docstring for binHeap"""
	def __init__(self):
		self.heaplist = [0]
		self.currentsize = 0

	def percUp(self,i):
		while i // 2 > 0:
			if self.heaplist[i//2] > self.heaplist[i]:
				self.heaplist[i//2],self.heaplist[i] \
				= self.heaplist[i],self.heaplist[i//2]
			i //= 2

	def insert(self,k):
		self.heaplist.append(k)
		self.currentsize += 1
		self.percUp(self.currentsize)

	def percDown(self,i):
		while (2 * i) <= self.currentsize:
			mc = self.minChild(i)
			if self.heaplist[i] > self.heaplist[mc]:
				tmp = self.heaplist[i]
				self.heaplist[i] = self.heaplist[mc]
				self.heaplist[mc] = tmp
			i = mc

	def minChild(self,i):
		if i * 2 + 1 > self.currentsize:
			return i * 2
		else:
			if self.heaplist[i*2] < self.heaplist[i*2+1]:
				return i * 2
			else:
				return i * 2 + 1

	def delMin(self):
		retval = self.heaplist[1]
		self.heaplist[1] = self.heaplist[self.currentsize]
		self.currentsize -= 1
		self.heaplist.pop()
		self.percDown(1)
		return retval

	def buildHeap(self,array):
		i = len(array) // 2
		self.currentsize = len(array)
		self.heaplist = [0] + array[:]
		while i > 0:
			self.percDown(i)
			i -= 1

#------------------------------二叉查找树------------------------------
class treeNode:
	"""docstring for treeNode"""
	def __init__(self, key, value, left=None, right=None, parent=None):
		self.key = key
		self.payload = value
		self.leftchild = left
		self.rightchild = right
		self.parent = parent

	def hasLeftChild(self):
		return self.leftchild

	def hasRightChild(self):
		return self.rightchild

	def isLeftChild(self):
		return self.parent and self.parent.leftchild == self

	def isRightChild(self):
		return self.parent and self.parent.rightchild == self

	def isRoot(self):
		return not self.parent

	def isLeaf(self):
		return not (self.rightchild or self.leftchild)

	def hasAnyChildren(self):
		return self leftchild or self.rightchild

	def hasBothChildren(self):
		return self.leftchild and self.rightchild

	def replaceNodeData(self,key,value,lc,rc):
		self.key = key 
		self.payload = value
		self.leftchild = lc
		self.rightchild = rc
		if self.hasLeftChild():
			self.leftchild.parent = self
		if self.hasRightChild():
			self.rightchild.parent = self

class binarySearchTree:
	"""docstring for binarySearchTree"""
	def __init__(self):
		self.root = None
		self.size = 0

	def length(self):
		return self.size

	def __len__(self):
		return self.size

	def __iter__(self):
		return self.root.__iter__()

	#递归创建子树
	def put(self,key,val):
		if self.root:
			self._put(key,value,self.root)
		else:
			self.root = treeNode(key,value)
		self.size += 1

	def _put(self,key,value,currentNode):
		if key == currentNode.key:
			currentNode.key = key
		elif key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,value,currentNode.leftchild)
			else:
				currentNode.leftchild = treeNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key,value,currentNode.rightchild)
			else:
				currentNode.rightchild = treeNode(key,value,parent=currentNode)

	def __setitem__(self,key,value):
		self.put(key,value)

	#递归检索子树
	def get(self,key):
		if self.root:
			res = self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	def _get(self,key,currentNode):
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif currentNode.key > key:
			return self._get(currentNode.getRightChild())
		else:
			return self._get(currentNode.getRightChild())

	def __getitem__(self,key):
		return self.get(key)

	#判断是否含有子树“in”操作
	def __contains__(self,key):
		if self._get(key,self.root):
			return true
		else:
			return False

	#删除子树键
	def delete(self,key):
		if self.size > 1:
			nodetoRemove = self._get(key,self.root)
			if nodetoRemove:
				self.remove(nodetoRemove)
				self.size -= 1
			else:
				raise KeyError("Error, key not in tree")
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size -= 1
		else:
			raise KeyError("Error, key not in tree")

	def __delitem__(self,key):
		self.delete(key)

	def findSuccessor(self):
		succ = None
		if self.hasRightChild():
			succ = self.rightchild.findMin()
		else:
			if self.parent:
				if self.isLeftChild():
					succ = self.parent
				else:
					self.parent.rightchild = None
					succ = self.parent.findSuccessor()
					self.parent.rightchild = self
		return succ

	def findMin(self):
		current = self
		while currentNode.hasLeftChild():
			current = current.leftchild
		return current

	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftchild = None
			else:
				self.parent.rightchild = None
		elif self.hasAnyChildren():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftchild = self.leftchild
				else:
					self.parent.rightchild = self.leftchild
				self.leftchild.parent = self.parent
			else:
				if self.isleftChild():
					self.parent.leftchild = self.rightchild
				else:
					self.parent.rightchild = self.rightchild
				self.rightchild.parent = self.parent

	def remove(self,currentNode):
		if currentNode.isLeaf():
			if currentNode == currentNode.parent.leftchild:
				currentNode.parent.leftchild = None
			else:
				currentNOde.parent.rightchild = None
		elif currentNode.hasBothChildren():
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key = succ.key
			currentNode.payload = succ.payload
		else:
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
					currentNode.leftchild.parent = currentNode.parent
					currentNode.parent.leftchild = currentNode.leftchild
				elif currentNode.isRightChild():
					currentNode.leftchild.parent  = currentNode.parent
					currentNode.parent.rightchild = currentNode.leftchild
				else:
					currentNode.replaceNodeData(currentNode.leftchild.key,
						currentNode.leftchild.payload,currentNode.leftchild.leftchild,
						currentNode.leftchild.rightchild)
			elif currentNode.hasRightChild():
				if currentNode.isLeftChild():
					currentNode.rightchild.parent = currentNode.parent
					currentNode.parent.leftchild = currentNode.rightchild
				elif currentNode.isRightChild():
					currentNode.rightchild.parent = currentNode.parent
					currentNode.parent.rightchild = currentNode.rightchild
				else:
					currentNode.replaceNodeData(currentNode.rightchild.key,
						currentNode.rightchild.payload, currentNode.rightchild.leftchild,
						currentNode.rightchild.rightchild)

#------    -------AVL树/平衡二叉搜索树--------------------------
#重写_put方法
def _put(self,key,value, currentNode):
	if key < currentNode.key:
		if currentNode.hasLeftChild():
			self._put(key, value, currentNode.leftchild)
		else:
			currentNode.leftchild = treeNode(key, value, parent=currentNode)
			self.updateBalance(currentNode.leftchild)
	else:
		if currentNode.hasRightChild():
			self._put(key, value, currentNode.rightchild)
		else:
			currentNode.rightchild = treeNode(key, value, parent=currentNode)
			self.updateBalance(currentNode.rightchild)

def updateBalance(self,node):
	if node.balanceFactor > 1 or node.balanceFactor	< -1:
		self.rebalance(node)
		return
	if node.parent != None:
		if node.isLeftChild():
			node.parent.balanceFactor += 1
		elif node.isRightChild():
			node.parent.balanceFactor -= 1
		if node.parent.balanceFactor != 0:
			self.updateBalance(node.parent)

def rotateLeft(self,rotRoot):
	newRoot = rotRoot.rightChild #临时变量存储旧根节点的右孩子
	# 设置旧根节点与新根节点左孩子节点间关系
	rotRoot.rightChild = newRoot.leftChild #旧根节点右孩子设置为新根子节点的左孩子
	if newRoot.leftChild != None:
		newRoot.leftChild.parent = rotRoot #新根节点左孩子父节点设置为旧根节点
	# 设置新根节点与旧根节点父节点间关系
	newRoot.parent = rotRoot.parent #新根节点父节点为旧根节点父节点
	if rotRoot.isRoot(): #旧根节点父节点的孩子节点判断/链接
		self.root = newRoot
	else:
		if rotRoot.isLeftChild():
	        rotRoot.parent.leftChild = newRoot
		else:
		    rotRoot.parent.rightChild = newRoot
	# 设置旧根节点与新根节点间关系
	newRoot.leftChild = rotRoot
	rotRoot.parent = newRoot
	
	rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
	newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

def rebalance(self,node):
	if node.balanceFactor < 0:
		if node.rightChild.balanceFactor > 0:
			self.rotateRight(node.rightChild)
			self.rotateLeft(node)
		else:
			self.rotateLeft(node)
	elif node.balanceFactor > 0:
		if node.leftChild.balanceFactor < 0:
			self.rotateLeft(node.leftChild)
			self.rotateRight(node)
		else:
			self.rotateRight(node)






		



