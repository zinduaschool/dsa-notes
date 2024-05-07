import AdjacencyList
from collections import deque

adjacency = AdjacencyList.Graph


my_graph = adjacency()

my_graph.add_vertex(1)
my_graph.add_vertex(2)
my_graph.add_vertex(3)
my_graph.add_vertex(4)
my_graph.add_edge(1, 3)
my_graph.add_edge(2, 3)
my_graph.add_edge(1, 4)
my_graph.show_graph()

'''
Traversal algorithms in Graphs.

DFS:(Stacks)/(Recursion)

BFS: (Queues)

//Insert the queue (it should not be empty-> insert the first node)
//Have a tracking list (To track the items that have been traversed)
//insert the starting point inside the tracking list
//Loop as long as the queue is not empty:
           //pop the first vertice in the queue
           //process the vertice at that time (Print statement)
           //loop to go through each of it's adjacent node(node being processed at that time)
                //check if the adjacent nodes are in the visited list(Tracking list)
                   //insert the adjacent vertices inside the queue
                    //insert the adjacent vertices inside the visited list.


'''

def bfs(graph, start_vertex):
    queue = deque([start_vertex])
    visited_vertices = set() #Only takes unique items (No repetition)
    visited_vertices.add(start_vertex)

    while queue: #check if the queue is empty or not
        popped = queue.popleft()
        print(popped)

        for adjacent in graph.adjacency_list[popped]:
            if adjacent not in visited_vertices:
                queue.append(adjacent)
                visited_vertices.add(adjacent)

bfs(my_graph, 1)








'''
Adjacency List
1 -> [3, 4]
2 -> [3]
3 -> [1, 2]
4 -> [1]
'''
