import math


class RadialLayout:
    def __init__(self, graph, alfa=0, beta=2 * math.pi, circumference=10, delta=1):
        """
        Creates a radial layout based on the radial positions algorithm
        by Andrew Pavlo by creating a copy of the given graph and
        adding coordinates into each node of the graph.
        
        Parameters:
            graph (dict): Dictionary representation of a graph
            alfa (float): Angle (radians) used to define the annulus wedge of
                the root node. Default: 0
            beta (float): Angle (radians) used to define the annulus wedge of
                the root node. Default: 2 * pi (~360 degrees)
            circumference (int): circumference of the radial layout. Default: 10.
            delta (int): Delta angle constant of the layouts concentric
                circles. Default: 1.
        """
        self.graph = graph
        self.updated_graph = {}
        self.x_coordinates = []
        self.y_coordinates = []

        if not self.graph: return

        self.get_coordinates(graph, graph['root'], alfa, beta, circumference, delta)

    def get_leaf_count(self, root):
        """
        Finds the number of nodes with no children - AKA 'leaves' -
        in a given sub-area of the graph using BFS.
        
        Parameters:
            root (str): Node name representing the root, or the starting
            point of this BFS search.

        Returns:
            leaf_count (int): The same dictionary representation as
            the inputted graph (dict), but with added coordinates

        """

        if not root: return 0

        visited, queue = [], []
        leaf_count = 0

        visited.append(root)
        queue.append(root)

        while queue:
            current_node = queue.pop(0)
            # If no child nodes, increase leaf count
            if len(self.graph[current_node['id']]['children']) == 0:
                leaf_count += 1

            # if child nodes, add all of them to the queue
            for node in self.graph[current_node['id']]['children']:
                if node not in visited:
                    visited.append(self.graph[node['id']])
                    queue.append(self.graph[node['id']])

        return leaf_count

    def get_coordinates(self, tree, node, alfa, beta, circumference, delta):
        """
        Appends coordinates to every node on the graph given when creating
        this object.
        
        Parameters:
            tree (dict): Current part of the graph
            node (dict): Current node
            alfa (float): Angle (radians) used to define the annulus wedge of
                the root node. Default: 0
            beta (float): Angle (radians) used to define the annulus wedge of
                the root node. Default: 2 * pi (~360 degrees)
            circumference (int): circumference of the radial layout. Default: 10.
            delta (int): Delta angle constant of the layouts concentric
                circles. Default: 1.
        """
        
        # If the root node
        if not node['parent']:
            node['position'] = { 'x': 0, 'y': 0 }
            self.updated_graph[node['id']] = node
            self.x_coordinates.append(0)
            self.y_coordinates.append(0)

        # Calculate radius for the root node
        theta = alfa
        root_radius = circumference / (2 * math.pi)
        radius = root_radius + (delta * node['depth'])

        # leaf count of the whole graph
        leaf_count = self.get_leaf_count(node)

        for child_node in node['children']:
            child_leaf_count = self.get_leaf_count(child_node)
            # Calculate a new angle value - in radians - to define the
            # annulus wedge of this node
            mi = theta + (child_leaf_count / leaf_count * (beta - alfa))

            # Get the x and y coordinates of the current node and
            # append them to the updated graph
            x = radius * math.cos((theta + mi) / 2.0)
            y = radius * math.sin((theta + mi) / 2.0)
            child_node['position'] = { 'x': x, 'y': y }

            self.updated_graph[child_node['id']] = child_node
            self.x_coordinates.append(x)
            self.y_coordinates.append(y)

            # If this node has children, get coordinates for them
            if len(self.graph[child_node['id']]['children']) > 0 :
                self.get_coordinates(
                    tree,
                    self.graph[child_node['id']],
                    theta,
                    mi,
                    circumference,
                    delta
                )
            
            # Update the theta (the new alfa) to equal mi (the new beta)
            theta = mi
