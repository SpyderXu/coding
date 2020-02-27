import queue
class Graph:
    def __init__(self, N):
        self.N = N
        self.graph = [set() for i in range(N)]
        self.visited = [0 for col in range(N)]
        self.inDegree = [0 for col in range(N)]
        self.pq = queue.PriorityQueue()
        self.top_sort_list = []
    
    def add_egde(self, eg):
        self.graph[eg[0]].add(eg[1])
        self.inDegree[eg[1]] += 1
    
    def add_edges(self, edges):
        for eg in edges:
            self.add_egde(eg)
    
    def top_sort(self, ):
        for i in range(self.N):
            if self.visited[i] == 0 and self.inDegree[i] == 0:
                self.pq.put(i)
        while not self.pq.empty():
            front = self.pq.get()
            self.visited[front] = 1
            self.top_sort_list.append(front)
            for child in self.graph[front]:
                self.inDegree[child] -= 1
                if self.inDegree[child] == 0:
                    self.pq.put(child)
        return self.top_sort_list