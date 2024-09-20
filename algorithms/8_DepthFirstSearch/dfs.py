# function for depth first search
def dfs(data, start, visited=set()):

    # if not visited print it
    if start not in visited:
        print(start, end=" ")

    visited.add(start)

    for i in data[start] - visited:

        # if not visited gi in depth of it
        dfs(data, i, visited)
    return


# sample data in dictionary form
data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
        }

#example 2
def dfs(graph,start,visited=None):
    if visited is None:
        visited = set() 
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph,next,visited) 
    return visited    


 

if __name__ == '__main__':

    dfs(data, 'A')
    graph = {'0': set(['1', '2']),
                '1': set(['0', '3', '4']),
                '2': set(['0']),
                '3': set(['1']),
                '4': set(['2', '3'])}

    dfs(graph, '0')   