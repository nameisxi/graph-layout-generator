import math


class RadialLayout:
    def __init__(self, graph, circumference=10):
        self.graph = graph
        self.x_coordinates = []
        self.y_coordinates = []

        if not self.graph: return

        alpha = 0
        beta = 2 * math.pi   
        delta = 1
        self.updated_graph = {}

        self.get_coordinates(graph, graph['root'], alpha, beta, circumference, delta)

    def bfs(self, root):
        if not root: return 0

        visited, queue = [], []
        leaves = 0

        visited.append(root)
        queue.append(root)

        while queue:
            current_node = queue.pop(0)
            if len(self.graph[current_node['id']]['children']) == 0: leaves += 1

            for node in self.graph[current_node['id']]['children']:
                if node not in visited:
                    visited.append(self.graph[node['id']])
                    queue.append(self.graph[node['id']])

        return leaves

    def get_coordinates(self, tree, node, alfa, beta, circumference, delta):
        if not node['parent']:
            node['position'] = { 'x': 0, 'y': 0 }
    
            self.updated_graph[node['id']] = node
            self.x_coordinates.append(0)
            self.y_coordinates.append(0)

        theta = alfa
        root_radius = circumference / (2 * math.pi)
        radius = root_radius + (delta * node['depth'])

        leaf_count = self.bfs(node)

        for child_node in node['children']:
            lambda_value = self.bfs(child_node)
            mi = theta + (lambda_value / leaf_count * (beta - alfa))

            x = radius * math.cos((theta + mi) / 2.0)
            y = radius * math.sin((theta + mi) / 2.0)
            child_node['position'] = { 'x': x, 'y': y }

            self.updated_graph[child_node['id']] = child_node
            self.x_coordinates.append(x)
            self.y_coordinates.append(y)

            if len(self.graph[child_node['id']]['children']) > 0 :
                self.get_coordinates(tree, self.graph[child_node['id']], theta, mi, circumference, delta)
            
            theta = mi
