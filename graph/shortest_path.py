#--encoding:utf-8--

#最短路徑
from bag import Bag
from graph_visualized import EdgeDigraphVisualized 

#无效的float
Infinity   = float("inf")


class DirectedEdge(object):
    _from = None
    _to = None
    _weight = None

    def __init__(self, v, w, weight):
        super(DirectedEdge, self).__init__()
        self._from = v        
        self._to = w        
        self._weight = weight

    def weight(self):
        return self._weight

    def fromV(self):
        return self._from

    def toV(self):
        return self._to

    def __str__(self):
        return "[vertex] %d-%d\t\t[weight] %.2f" % (self._from, self._to, self._weight)


class EdgeWeightDigraph(object):
    #顶点数量
    num_vertexCnt = 0
    #边的数量
    num_edgeCnt = 0
    #邻接表
    arr_adj = None 

    def __init__(self, intext=None, vCnt=None):
        super(EdgeWeightDigraph, self).__init__()

        if intext == None:
            self.num_vertexCnt = vCnt
            self.num_edgeCnt = 0
            self.arr_adj = [Bag() for i in range(self.num_vertexCnt)]
        else:
            lines = intext.split('\n')
            vertexCnt = int(lines[0])
            self.num_vertexCnt = vertexCnt
            self.num_edgeCnt = 0
            self.arr_adj = [Bag() for i in range(self.num_vertexCnt)]
            for x in range(1,len(lines)):
                vs = lines[x].split('-')
                v0 = int(vs[0])
                v1 = int(vs[1])
                v2 = float(vs[2])
                edge = DirectedEdge(v0, v1, v2)
                self.AddEdge(edge)

    def AddEdge(self, edge):
        self.arr_adj[edge.fromV()].Add(edge)

    def V(self):
        return self.num_vertexCnt

    def E(self):
        return self.num_edgeCnt

    def adj(self, v):
        return self.arr_adj[v]

    def Printf(self, fileName):
        EdgeDigraphVisualized().printf(self, fileName)
        pass


#迪杰斯特拉算法(贪心算法)
class DijkstraSP(object):
    #加权有向图
    digraph = None
    #起点
    s = None
    #父链接数组(edgeTo[V],连接v和它的父节点的边, 假如v是终点, edgeTo[v]就是最后一条边)
    _edgeTo = None
    #到起点的距离
    _distTo = None
    #优先队列
    _pq = None

    def __init__(self, digraph, s):
        super(DijkstraSP, self).__init__()
        self.digraph = digraph
        self.s = s
        self._edgeTo = [None for i in range(digraph.V())]
        self._distTo = [Infinity for i in range(digraph.V())]
        self._distTo[s] = 0
        self._pq = []
        self._pq.append(s)
        while len(self._pq) > 0:
            top = self._pq[0]
            self._pq.pop(0)
            self.relax(digraph, top)
            pass

    def relax(self, G, V):
        for bag in G.adj(V):
            edge = bag.value 
            w = edge.toV()
            if self.distTo(w) > self.distTo(V) + edge.weight():
                #放松边
                self._distTo[w] = self.distTo(V) + edge.weight()
                self._edgeTo[w] = edge
                #
                if w in self._pq:
                    #交换,降低优先级
                    wIdx = self._pq.index(w)
                    toIdx = self._pq.pop(wIdx)
                    self._pq.append(w)
                else:
                    #插入
                    self._pq.append(w)


    def distTo(self, v):
        return self._distTo[v]

    def hasPathTo(self, v):
        return v < len(self._distTo) and self._distTo[v] < Infinity

    def pathTo(self, v):
        p = []
        p.append(v)
        while v != self.s and self._edgeTo[v] != None:
            v = self._edgeTo[v].fromV()
            p.append(v)
        p.reverse()
        return '->'.join([str(x) for x in p])


#--------------------------------test-------------------------------------
str_digraph = "8\n\
4-5-0.35\n\
5-4-0.35\n\
4-7-0.37\n\
5-7-0.28\n\
7-5-0.28\n\
5-1-0.32\n\
0-4-0.38\n\
0-2-0.26\n\
7-3-0.39\n\
1-3-0.29\n\
2-7-0.34\n\
6-2-0.40\n\
3-6-0.52\n\
6-0-0.58\n\
6-4-0.93"




if __name__ == '__main__':
    digraph = EdgeWeightDigraph(intext = str_digraph)
    # digraph.Printf("shortest")
    dijkstraSP = DijkstraSP(digraph, 0)
    print(dijkstraSP.hasPathTo(6))
    print(dijkstraSP.pathTo(6))