#--encoding:utf-8--

from bag import Bag
from graph_visualized import MSTVisualized 

class Edge(object):
    _v = None
    _w = None
    _weight = None
    _black = None

    def __init__(self, v, w, weight):
        super(Edge, self).__init__()
        self._v = v        
        self._w = w        
        self._weight = weight
        self._black = False       

    def markBlack(self):
        self._black = True

    def IsBlack(self):
        return self._black

    def weight(self):
        return self._weight

    #边的一个顶点
    def either(self):
        return self._v

    def other(self, v):
        if self._v == v:
            return self._w
        elif self._w == v:
            return self._v
        else:
            raise Exception(print("不存在顶点...."))            

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __le__(self, other):
        return self.weight() <= other.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __ge__(self, other):
        return self.weight() >= other.weight()

    def __eq__(self, other):
        return self.weight() == other.weight()

    def __str__(self):
        return "[vertex] %d-%d\t\t[weight] %.2f" % (self._v, self._w, self._weight)

class EdgeWeightGraph(object):
    #顶点数量
    num_vertexCnt = 0
    #边的数量
    num_edgeCnt = 0
    #邻接表
    arr_adj = None 

    def __init__(self, intext = None, vCount = None):
        super(EdgeWeightGraph, self).__init__()

        if intext == None:
            self.num_vertexCnt = vCount
            self.arr_adj = [Bag() for i in range(self.num_vertexCnt)]
            self.num_edgeCnt = 0
        else:
            lines = intext.split('\n')
            self.num_vertexCnt = int(lines[0])
            self.num_edgeCnt = 0
            self.arr_adj = [Bag() for i in range(self.num_vertexCnt)]
            for x in range(1,len(lines)):
                vs = lines[x].split('-')
                v0 = int(vs[0])
                v1 = int(vs[1])
                v2 = float(vs[2])
                edge = Edge(v0, v1, v2)
                self.AddEdge(edge)

    def AddEdge(self, edge):
        v = edge.either()
        w = edge.other(v)
        self.arr_adj[v].Add(edge)
        self.arr_adj[w].Add(edge)


    def V(self):
        return self.num_vertexCnt

    def E(self):
        return self.num_edgeCnt

    def adj(self, v):
        return self.arr_adj[v]

    def Printf(self, fileName):
        MSTVisualized(False).printf(self, fileName)


#Prim算法  一开始添加一个顶点， 然后添加一条它邻接的最小边，把这条边的两个顶点都加到树里面，然后继续寻找最小的邻接边直到找到V-1条边
class PrimMST(object):
    graph = None
    #最小生成树的顶点
    marked = None
    #最小生成树的边
    edgeQueue = None
    #横切边
    pq = None

    """docstring for PrimMST"""
    def __init__(self, graph):
        super(PrimMST, self).__init__()
        self.graph = graph
        self.marked = [False for i in range(graph.V())]
        self.edgeQueue = []
        self.pq = []

        self.visit(0)
        while len(self.pq) > 0:
            minEdge = self.pq[0]
            self.pq.pop(0)
            vv = minEdge.either()
            vw = minEdge.other(vv)
            if not self.marked[vv] or not self.marked[vw]:
                self.edgeQueue.append(minEdge)
                if not self.marked[vv]:
                    self.visit(vv)
                if not self.marked[vw]:
                    self.visit(vw)
                
        genGraph = EdgeWeightGraph(vCount=graph.V())
        for edge in self.edgeQueue:
            genGraph.AddEdge(edge)
        genGraph.Printf("mst_gen")

    def visit(self, v):
        self.marked[v] = True
        for edgeWrap in self.graph.adj(v):
            edge = edgeWrap.value
            if not self.marked[edge.other(v)]:
                self.pq.append(edge)

        self.pq.sort(key=lambda x:x.weight())
        # self.pq.reverse()

#MST (Minimum Spanning Tree)

#----------------------------Test--------------------------------------
str_graph = "8\n\
4-5-0.35\n\
4-7-0.37\n\
5-7-0.28\n\
0-7-0.16\n\
1-5-0.32\n\
0-4-0.38\n\
2-3-0.17\n\
1-7-0.19\n\
0-2-0.26\n\
1-2-0.36\n\
1-3-0.29\n\
2-7-0.34\n\
6-2-0.40\n\
3-6-0.52\n\
6-0-0.58\n\
6-4-0.93"

graph = EdgeWeightGraph(intext = str_graph)
graph.Printf("mst_origin")
PrimMST(graph)