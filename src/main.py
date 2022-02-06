import sys
import json

from layout_generator import LayoutGenerator


def read_graph(file_path):
    """
    Reads a graph from a JSON file based on the given file path
    
    Parameters:
        file_path (str): Path to the JSON file containing the graph

    Returns:
        graph (dict): Dictionary containing the JSON file's contents
    """
    # Prepare the file path by stripping any possible whitespace.
    file_path = file_path.strip()
    # If the given file path is empty, use the example graph's path instead
    if not file_path: file_path = 'example_graph.json'

    try:
        # Attempt to open the JSON file containing the graph
        with open(file_path) as file:
            return json.load(file)
    except Exception as e:
        print("While trying to read the graph, the following exception occured:")
        print(e)


def main():
    # Get the path to the JSON file that defines the structure of the graph 
    # that the user wants to generate a layout for. Then, read the graph. 
    print("-"*50)
    print()
    file_path = input("Graph file path (press Enter to use the example graph): ")
    graph = read_graph(file_path)

    # Create a LayoutGenerator object that handles the creation of different
    # kinds of layouts. As a default, it generates a radial layout.
    layout_generator = LayoutGenerator()
    updated_graph = layout_generator.create_layout(graph)

    # Print the updated graph, that contains the coordinates, to the user 
    print()
    print("-"*50)
    print("Graph with coordinates:")
    print()
    print(json.dumps(updated_graph, sort_keys=True, indent=4))
    print()
    print("-"*50)

    sys.exit()


if __name__ == "__main__":
    main()
