class edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
    
    def either(self, ):
        return self.u
    
    def other(self, p):
        if self.u == p:
            return self.v
        else:
            return self.u
    
    def __lt__(self, other):
        return self.w < other.w

class PrimMST:
    def __init__(self, N):
        self.graph = [set() for i in range(N)]
        self.N = N
        self.marked = [0 for i in range(N)]
        self.pq = queue.PriorityQueue()
        self.mst = queue.Queue()
    
    def add_egde(self, eg):
        u = eg.either()
        v = eg.other(u)
        self.graph[u].add(eg)
        self.graph[v].add(eg)
    
    def add_edges(self, egs):
        for eg in egs:
            self.add_edge(eg)
    
    def visit(self, v):
        self.marked[v] = 1
        for eg in self.graph[v]:
            u = eg.other(v)
            if self.marked[u] == 0:
                self.pq.put(eg)
    
    def get_mst(self):
        self.visit(0)
        while not self.pq.empty():
            front = self.pq.get()
            u = front.either()
            v = front.other()
            if self.marked[u] and self.marked[v]:
                continue
            self.mst.put(front)
            if self.marked[u] == 0:
                self.visit(u)
            if self.marked[v] == 0:
                self.visit(v)
        return self.mst