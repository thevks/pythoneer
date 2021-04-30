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
                return self.find_path(node, end, path)
    
    def bfs(self, start_node):
        queue = [start_node]
        visited = [start_node]
        while queue:
            n = queue.pop(0)
            for node in self.dict[n]:
                if node not in visited:
                    visited.append(node)
                    queue.append(node)
            print(n, end = " ")
    
    def dfs(self, start_node):
        stack = [start_node]
        visited = [start_node]
        while stack:
            n = stack.pop(len(stack)-1)
            for node in self.dict[n]:
                if node not in visited:
                    visited.append(node)
                    stack.append(node)
            print(n)
    
    def shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.dict:
            return None
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
    #g = Graph()
    #g.add_edge(1,2)
    #g.add_edge(1,3)
    #g.add_edge(2,3)
    #g.add_edge(2,1)
    #g.add_edge(3,1)
    #g.add_edge(3,2)
    #g.add_edge(3,4)
    #g.add_edge(4,3)

    #g.show_edges()
    
    #print(g.find_path(4,1))
    #g.bfs(3)
    #g.dfs(3)
    #print(g.shortest_path(2,3))
    #g.bfs(1)
    #g.dfs(1)
    #print(g.all_paths(2,3))
    #print(g.shortest_path(2,4))
    b = Graph()
    b.add_edge('a','b')
    b.add_edge('a','c')
    b.add_edge('b','d')
    b.add_edge('b','e')
    b.add_edge('b','f')
    b.add_edge('c','g')
    b.add_edge('c','h')
    b.add_edge('c','i')
    b.add_edge('c','j')
    b.add_edge('j','k')

    b.add_edge('d','b')
    b.add_edge('e','b')
    b.add_edge('f','b')

    b.add_edge('g','c')
    b.add_edge('h','c')
    b.add_edge('i','c')
    b.add_edge('j','c')
    
    b.add_edge('k','j')
    

    #b.show_edges()
    #b.bfs('a')
    b.shortest_path('a','k')
    