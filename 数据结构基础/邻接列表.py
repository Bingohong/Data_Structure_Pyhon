#-------------------------图结构-----------------
#邻接列表构成图
#vertex为顶点信息，connectionto字典记录顶点间连接关系和边权重
class vertex:
	"""docstring for vertex"""
	def __init__(self, key):
		self.id = key
		self.connectionto = {}

	def addNeighbor(self,nbr,weight=0):
		self.connectionto[nbr] = weight

	def __str__(self):
		return str(self.id) + " connectionto: " + str([x.id for x in self.connectionto])

	def getConnections(self):
		return self.connectionto.keys()

	def getId(self):
		return self.id

	def getWeight(self,nbr):
		return self.connectionto[nbr]

#graph，verlist字典包含所有顶点对象
class graph:
	"""docstring for graph"""
	def __init__(self):
		self.vertList = {}
		self.numVertices = 0

	def addVertex(self,key):
		self.numVertices += 1
		newVertex = vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self,n):
		if n in self.vertList:
			return self.vertList[n]
		else:
			return None

	def __contains__(self,n):
		return n in self.vertList

	def addEdge(self,f,t,cost=0):
		if f not in self.vertList:
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)
		self.vertList[f].addNeighbor(self.vertList[t],cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):# 创建可迭代对象及方法
		return iter(self.vertList.values())

# ----------------------------------图结构实例-------------------------
#字梯
def buildGraph(wordFile):
	d = {}
	g = graph()
	wfile = open(wordFile,"r")
	for line in wfile:
		word = line[:-1]
		for i in range(len(word)):
			bucket = word[:i] + "_" + word[i+1:]
			if bucket in d:
				d[bucket].append(word)
			else:
				d[bucket] = [word]
	for bucket in d.keys():
		for word1 in d[bucket]:
			for word2 in d[bucket]:
				if word1 != word2:
					g.addEdge(word1,word2)
	return g

#广度优先算法(BFS)
#扩展vertex类
class Vertex:
    def __init__(self,num):
        self.id = num
        self.connectedTo = {}
        self.color = 'white'
        self.dist = sys.maxsize
        self.pred = None
        self.disc = 0
        self.fin = 0
    
    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight
        
    def setColor(self,color):
        self.color = color
        
    def setDistance(self,d):
        self.dist = d

    def setPred(self,p):
        self.pred = p

    def setDiscovery(self,dtime):
        self.disc = dtime
        
    def setFinish(self,ftime):
        self.fin = ftime
        
    def getFinish(self):
        return self.fin
        
    def getDiscovery(self):
        return self.disc
        
    def getPred(self):
        return self.pred
        
    def getDistance(self):
        return self.dist
        
    def getColor(self):
        return self.color
    
    def getConnections(self):
        return self.connectedTo.keys()
        
    def getWeight(self,nbr):
        return self.connectedTo[nbr]
                
    def __str__(self):
        return str(self.id) + ":color " + self.color + ":disc " + str(self.disc) + ":fin " + str(self.fin) + ":dist " + str(self.dist) + ":pred \n\t[" + str(self.pred)+ "]\n"
    
    def getId(self):
        return self.id

# distance记录距离
# predecessor记录前导节点
# color标记处理程度：white、black、gray
def bfs(g,start):
	start.setDistance(0)
	start.setPred(None)
	vertQueue = Queue()
	vertQueue.enqueue(start)
	while (vertQueue.size() > 0):
		currentVert =  vertQueue.dequeue()
		for nbr in currentVert.getConnections():
			if (nbr.getColor() == "white"):
				nbr.setColor("gray")
				nbr.setDistance(currentVert.getDistance + 1)
				nbr.setPred(currentVert)
				vertQueue.enqueue(nbr)#队列结构
		currentVert.setColor("black")

def traverse(y):#根据前导节点predecessor构建广度优先树
	x = y
	while x.getPred():
		print(x.getId())
		x = x.getPred()
	print(x.getId())

# ---------------------------深度优先搜索算法---------------------
# discoverytime记录发现时间
# finishtime记录扫描完成时间
# 扩展Graph类
class DFSGraph(Graph):
	"""docstring for DFSGraph"""
	def __init__(self):
		super().__init__()
		self.time = 0

	def dfs(self):
		for aVertex in self:
			aVertex.setColor("white")
			aVertex.pred(-1)
		for aVertex in self:
			if aVertex.getColor() == "white":
				self.dfsvisit(aVertex)

	def dfsvisit(self,startVertex):
		startVertex.setColor("gray")
		self.time += 1
		startVertex.setDiscovery(self.time)
		for nextvert in startVertex.getConnections():
			if nextvert.getColor() == "white":
				nextvert.setPred(startVertex)
				#执行递归在更深级别搜索,栈结构
				self.dfsvisit(nextvert)
		startVertex.setColor("black")
		'''说明：
		深度优先树中的特定节点的所有子节点具有比
		它们的父节点更晚的发现时间和更早的完成时间
		'''
		self.time += 1 
		startVertex.setFinish(self.time)

	# 拓扑排序 - 表示任务间的依赖关系，约束任务完成顺序
	'''分析：
	可以将图进行深度优先搜索 (DFS)
	按完成时间递减顺序排序 (self.fin)
	排序结果即为拓扑排序结果
	'''
	def topological_sort(self):
		self.dfs()
		toposort = []
		for currentVert in self:
			topsort.append = currentVert
		# 选择排序
		n = len(topsort)
		for fillslot in range(n-1,0,-1):
			positionMin = 0
			for location in range(1,fillslot+1):
				if topsort[positionMin].getFinish() > topsort[location].getFinish():
					positionMin = location
			topsort[positionMin],topsort[fillslot] = topsort[fillslot],topsort[positionMin]
		return topsort

# -----------------------------有向无环图(DAG)最短路径----------------------------
# Dijkstra算法 - 构建单源最短路径树
from pythonds.graphs import PriorityQueue, Graph, Vertex
def dijkstra(agraph,start):
	pq = PriorityQueue()
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(),v) for v in agraph])
	while not pq.isEmpty():
		currentVert = pd.delMin()
		for nextvert in currentVert.getConnections():
			# 考虑新加入顶点更新其他点到源点距离，即nextvert顶点到源点的最短距离
			newdist = currentVert.getDistance() + currentVert.getWeight(nextvert)
			if newdist < nextvert.getDistance():
				nextvert.setDistance(newdist)
				nextvert.setPred(currentVert)
				pq.decreaseKey(nextvert,newdist)

# ----------------------------最小生成树-----------------------
# prim算法 - 所有边代价最小
def prim(agraph,start):
	pq = PriorityQueue()
	start.setDistance(0)
	pq.buildHeap([(v.getDistance(),v) for v in agraph])
	while not pq.isEmpty():
		currentVert = pq.delMin()
		for nextvert in currentVert:
			# 仅考虑相邻点权重，即顶点到生成树集合的距离最短
			cost = currentVert(nextvert)
			if cost < nextvert.getDistance():
				nextvert.setDistance(cost)
				nextvert.setPred(currentVert)
				pq.decreaseKey(nextvert)

# ----------------------------------强连通分量算法-------------------------------------
# 简化图表示 strongly connected components
'''分析
1.调用 dfs 为图 G 计算每个顶点的完成时间。
2.计算 G^T 。
3.为图 G^T 调用 dfs，但在 DFS 的主循环中，以完成时间的递减顺序探查每个顶点。
4.在步骤 3 中计算的森林中的每个树是强连通分量。输出森林中每个树中每个顶点的顶点标识组件。
'''
def scc(agraph):
	agraphsort = sorted(agraph,key=lambda x:x.getFinish(),reverse=True)
	transpose = transposeGraph(agraphsort)
	transpose.dfs()

def transposeGraph(agraph):
	transpose = DFSGraph()
	for vertex in agraph:
		for edge in vertex.getConnections():
			transpose.addEdge(edge.getId(),vertex.getId(),vertex.getWeight(edge))
	return transpose



		




		