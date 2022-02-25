from layouts import RadialLayout


class LayoutGenerator:
    def __init__(self, layout_type='radial'):
        """
        Creates a layout generator that can be used to create layouts once
        or more.
        
        Parameters:
            layout_type (str): Name of the layout to be used when creating
            a layout. Default value: 'radial'
        """

        self.layout_type = layout_type

    def create_layout(self, graph):
        """
        Creates a layout corresponding to the given layout type by
        adding coordinates to the graph that is inputted into this function.
        
        Parameters:
            graph (dict): Dictionary representation of a graph

        Returns:
            updated_graph (dict): The same dictionary representation as
            the inputted graph (dict), but with added coordinates

        """

        layout = None

        if self.layout_type == 'radial':
            layout = RadialLayout(graph)

        if not layout: return None

        return layout.updated_graph
