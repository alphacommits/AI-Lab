from queue import PriorityQueue
graph = {
    'A': [('B', 5), ('C', 7)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 3)],
    'D': [],
    'E': [('G', 6)],
    'F': [],
    'G': []
}

def uniform_cost_search(graph, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start, [start]))  # Insert start node with priority 0

    while not priority_queue.empty():
        cost, node, path = priority_queue.get()

        if node == goal:
            print('Goal found!')
            print('Path:', ' -> '.join(path))
            print('Total cost:', cost)
            return

        visited.add(node)

        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                priority_queue.put((new_cost, neighbor, new_path))

    print('Goal not found.')

start_node = 'A'
goal_node = 'G'
uniform_cost_search(graph, start_node, goal_node)