def bfs(data, start, visited=set()):

    queue = [start]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(current_node, end=" ")
        visited.add(current_node)

        for i in data[current_node] - visited:
            queue.append(i)
    return



#Example 2
# BFS algorithm in Python


import collections

# BFS algorithm
def bfs(graph, root):

    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:

        # Dequeue a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and
        # enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)





if __name__ == '__main__':

    data = {
        'A': {'B'}, 'B': {'A', 'C', 'D'}, 'C': {'B', 'E'}, 'D': {'B', 'E'},
        'E': {'C', 'D', 'F'}, 'F': {'E'}
    }

    bfs(data, 'A')


    
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal: ")
    bfs(graph, 0)




    