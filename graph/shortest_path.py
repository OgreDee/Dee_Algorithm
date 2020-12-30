#--encoding:utf-8--

#最短路徑
from bag import Bag
from graph_visualized import EdgeDigraphVisualized 


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


class SP(object):
    digraph = None
    s = None

    def __init__(self, digraph, s):
        super(SP, self).__init__()
        self.digraph = digraph
        self.s = s

    def distTo(self, v):
        pass

    def hasPathTo(self, v):
        pass

    def pathTo(v):
        pass
        


#--------------------------------test-------------------------------------
str_digraph = "8\n\
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



if __name__ == '__main__':
    digraph = EdgeWeightDigraph(intext = str_digraph)
    digraph.Printf("shortest")
