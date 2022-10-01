#breadth first search python code for finding the shortest path between Arad and Bucharest 

# graph is in adjacent list representation
graph = {
        'arad': ['sibiu', 'zerind', 'timisoara'],
        'sibiu': ['oradea', 'fagaras', 'rimnicu'],
        'zerind': ['arad', 'oradea'],
        'timisoara': ['arad', 'lugoj'],
        'oradea': ['zerind', 'sibiu'],
        'fagaras': ['sibiu', 'bucharest']
        }

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)
