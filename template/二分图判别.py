class Graph:
    def __init__(self, N):
        self.graph = [set() for col in range(N)]
        self.N = N
        self.visited = [0 for col in range(N)]
        self.colored = [0 for col in range(N)]
        self.bitable = True
    
    def add_edge(self, eg):
        self.graph[eg[0]].add(eg[1])
        self.graph[eg[1]].add(eg[0])
    
    def add_edges(self, egs):
        for eg in egs:
            self.add_edge(eg)
    
    def dfs(self, v):
        self.visited[v] = 1
        for child in self.graph[v]:
            if self.visited[child] == 0:
                self.colored[child] = self.colored[v]*(-1)
                self.dfs(child)
            else:
                if self.colored[v] == self.colored[child]:
                    self.bitable = False
    def judge_bitabe(self):
        for v in range(self.N):
            if self.visited[v] == 0:
                self.colored[v] = 1
                self.dfs(v)
                if self.bitable == False:
                    return False
        return True



