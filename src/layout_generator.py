from radial_layout import RadialLayout


class LayoutGenerator:
    def __init__(self, layout_type='radial'):
        self.layout_type = layout_type

    def create_layout(self, graph):
        layout = None

        if self.layout_type == 'radial':
            layout = RadialLayout(graph)
        
        return layout.updated_graph
