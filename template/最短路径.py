"""
Dijkstra 最短路径算法，查找一个点到其他点的最短的路径
"""
import queue
class edge:
    def __init__(self, s, e, w):
        self.s = s
        self.e = e
        self.w = w

    def src(self, ):
        return self.s

    def dst(self, ):
        return self.e

    def weight(self, ):
        return self.w

class elem:
    def __init__(self, v, dist):
        self.v = v
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist


class Graph:
    def __init__(self, N):
        self.graph = [[] for i in range(N)]
        self.distTo = [0 for row in range(N)]
        self.edgeTo = [None for row in range(N)]
        self.v = N
        self.visited = [0 for row in range(N)]
        self.pq = queue.PriorityQueue()

    def add_edge(self, eg):
        s = eg.src()
        self.graph[s].append(eg)

    def add_edges(self, egs):
        for eg in egs:
            self.add_edge(eg)

    def relax(self, v):
        self.visited[v] = 1
        for eg in self.graph[v]:
            e = eg.dst()
            if self.distTo[e] > self.distTo[v] + eg.weight():
                self.distTo[e] = self.distTo[v] + eg.weight()
                self.edgeTo[e] = eg
                self.pq.put(elem(e, self.distTo[e]))

    def get_nmp(self, p):
        self.distTo[p] = 0
        for i in range(self.v):
            if i != p:
                self.distTo[i] = float("inf")
        self.pq.put(elem(p, 0.0))
        while not self.pq.empty():
            front = self.pq.get()
            if self.visited[front.v] == 0:
                self.relax(front.v)