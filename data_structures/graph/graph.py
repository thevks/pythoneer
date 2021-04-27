class Graph:
    dict={}
    def add_edge(self, node, neighbour):
        if node not in self.dict:
            self.dict[node] = [neighbour]
        else:
            self.dict[node].append(neighbour)
    def show_edges(self):
        for node in self.dict:
            for neighbour in self.dict[node]:
                print(node, neighbour)
    
    def find_path(self, start, end, path=[]):
        path = path + [start]    
        if start == end:
            return path
        for node in self.dict[start]:
            if node not in path:
                newPath = self.find_path(node, end, path)
                if newPath:
                    return newPath
                return None

    def bfs(self, start_node):
        visited={}
        for i in self.dict:
            visited[i] = False
        queue = []
        queue.append(start_node)
        visited[start_node] = True
        while len(queue) != 0:
            start_node = queue.pop(0)
            for node in self.dict[start_node]:
                if visited[node] != True:
                    visited[node] = True
                    queue.append(node)
            print(start_node, end=" ")

    def dfs(self, start_node):
        visited = {}
        for i in self.dict:
            visited[i] = False
        stack = [start_node]
        visited [start_node] = True
        while stack:
            n = stack.pop(len(stack)-1)
            for i in self.dict[n]:
                if not visited[i]:
                    stack.append(i)
                    visited[i]=True
            print(n)
    
    def shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        shortest = None
        for node in self.dict[start]:
            if node not in path:
                newpath = self.shortest_path(node, end, path)
                if newpath:
                    if not shortest or len(shortest) > len(newpath):
                        shortest = newpath
        return shortest

    def all_paths(self, start, end, path = []):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.dict[start]:
            if node not in path:
              newpaths = self.all_paths(node, end, path)
              for newpath in newpaths:
                paths.append(newpath)
        return paths

if __name__ == '__main__' :
    g = Graph()
    g.add_edge(1,2)
    g.add_edge(1,3)
    g.add_edge(2,3)
    g.add_edge(2,1)
    g.add_edge(3,1)
    g.add_edge(3,2)
    g.add_edge(3,4)
    g.add_edge(4,3)

    g.show_edges()
    
    print(g.find_path(4,1))
    g.bfs(3)
    g.dfs(3)
    print(g.shortest_path(2,3))
    print(g.all_paths(2,3))