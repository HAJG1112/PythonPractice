class graph:
    
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
    '''
    algorithm traverses a graph in a depth ward motion and uses a stack 
    to remember to get the next vertex to start a search, when a dead end occurs 
    in any iteration. We implement DFS for a graph in python using the set data 
    types as they provide the required functionalities to keep track 
    of visited and unvisited nodes.
    '''
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

def bfs(graph, startnode):
    import collections
    '''
    BFS for a graph in python using queue data structure discussed earlier. 
    When we keep visiting the adjacent unvisited nodes and keep adding it to the queue. 
    Then we start dequeue only the node which is left with no unvisited nodes. 
    We stop the program when there is no next adjacent node to be visited.
    '''
    # Track the visited and unvisited nodes using queue
    seen, queue = set([startnode]), collections.deque([startnode])
    while queue:
        vertex = queue.popleft()
        marked(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

def marked(n):
    print(n)


class path_finder:
    def find_path(self, graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            if not start in graph:
                return None
            for node in graph[start]:
                if node not in path:
                    newpath = self.find_path(graph, node, end, path)
                    if newpath: return newpath
            return None

    def find_all_paths(self, graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return [path]
            if not start in graph:
                return []
            paths = []
            for node in graph[start]:
                if node not in path:
                    newpaths = self.find_all_paths(graph, node, end, path)
                    for newpath in newpaths:
                        paths.append(newpath)
            return paths
    def find_shortest_path(self, graph, start, end, path=[]):
            path = path + [start]
            if start == end:
                return path
            if not graph.has_key(start):
                return None
            shortest = None
            for node in graph[start]:
                if node not in path:
                    newpath = self.find_shortest_path(graph, node, end, path)
                    if newpath:
                        if not shortest or len(newpath) < len(shortest):
                            shortest = newpath
            return shortest

'''
This is a dictionary whose keys are the nodes of the graph. For each key, the corresponding value is a list
containing the nodes that are connected by a direct arc from this node. 
'''
gdict = { "a" : set(["b","c"]),
          "b" : set(["a", "d"]),
          "c" : set(["a", "d"]),
          "d" : set(["e"]),
          "e" : set(["a"])}

graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}     
p = path_finder()
print('DFS of gdict')
dfs(gdict, 'a')
print('BFS of gdict')
bfs(gdict, "a")
print('Find path')
print(p.find_path(graph, 'A', 'D'))
print('find all paths')
print(p.find_all_paths(graph, 'A', 'D'))