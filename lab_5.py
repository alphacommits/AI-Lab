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

heuristics = {
    'A': 10,
    'B': 7,
    'C': 8,
    'D': 6,
    'E': 4,
    'F': 3,
    'G': 0
}

def greedy_best_first_search(graph, heuristics, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((heuristics[start], start, [start]))  # Insert start node with priority = heuristic value

    while not priority_queue.empty():
        _, node, path = priority_queue.get()

        if node == goal:
            print('Goal found!')
            print('Path:', ' -> '.join(path))
            return

        visited.add(node)
        for neighbor, edge_cost in graph[node]:
            if neighbor not in visited:
                priority = heuristics[neighbor]  # Use the heuristic value for priority calculation
                new_path = path + [neighbor]
                priority_queue.put((priority, neighbor, new_path))

    print('Goal not found.')
start_node = 'A'
goal_node = 'G'
greedy_best_first_search(graph, heuristics, start_node, goal_node)