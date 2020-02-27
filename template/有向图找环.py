class Graph:
    def __init__(self, N):
        self.N = N
        self.graph = [set() for i in range(N)]
        self.visited = [0 for col in range(N)]
        self.onStack = [0 for col in range(N)]
        self.has_circle = False
        self.edgeTo = [i for i in range(N)]
        self.circle = []
    
    def add_edge(self, eg):
        self.graph[eg[0]].add(eg[1])
    
    def add_edges(self, egs):
        for eg in egs:
            self.add_edge(eg)
    
    def dfs(self, v):
        if self.has_circle:
            return
        self.visited[v] = 1
        self.onStack[v] = 1
        for child in self.graph[v]:
            if self.visited[child] == 0:
                self.edgeTo[child] = v
                self.dfs(child)
            else:
                if self.onStack[child] == 1:
                    self.has_circle = True
                    x = v
                    self.circle.append(v)
                    while x != child:
                        x = self.edgeTo[x]
                        self.circle.append(x)
        self.onStack[v] = 0
    
    def judge_circle(self, ):
        for v in range(self.N):
            if self.visited[v] == 0:
                self.dfs(v)
                if self.has_circle:
                    return True
        return False