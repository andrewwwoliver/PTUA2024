class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = set()

    def add_neighbor(self, neighbor_id):
        self.neighbors.add(neighbor_id)

    def get_connectivity(self):
        return len(self.neighbors)

    def __repr__(self):
        return f"Node {self.node_id}"


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_edge(self, node_id1, node_id2):
        node1 = self.nodes.setdefault(node_id1, Node(node_id1))
        node2 = self.nodes.setdefault(node_id2, Node(node_id2))

        node1.add_neighbor(node_id2)
        node2.add_neighbor(node_id1)

    def average_connectivity(self):
        total_connectivity = sum(node.get_connectivity() for node in self.nodes.values())
        return total_connectivity / len(self.nodes)

    def max_connectivity(self):
        max_connectivity = 0
        max_connectivity_nodes = []

        for node in self.nodes.values():
            connectivity = node.get_connectivity()
            if connectivity > max_connectivity:
                max_connectivity = connectivity
                max_connectivity_nodes = [node]
            elif connectivity == max_connectivity:
                max_connectivity_nodes.append(node)

        return max_connectivity, max_connectivity_nodes

    def min_connectivity(self):
        min_connectivity_nodes = [node for node in self.nodes.values() if node.get_connectivity() > 0]
        if not min_connectivity_nodes:
            return 0, []

        min_connectivity = min(node.get_connectivity() for node in min_connectivity_nodes)
        return min_connectivity, min_connectivity_nodes

    def disconnected_nodes(self):
        connected_nodes = set()

        for node in self.nodes.values():
            connected_nodes.update(node.neighbors)

        disconnected_nodes = [node for node_id, node in self.nodes.items() if node_id not in connected_nodes]
        return disconnected_nodes


def create_graph_from_gal(file_path):
    graph = Graph()

    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            unit_id = int(parts[0])

            # Handle invalid entries
            try:
                neighbors = [int(neighbor) for neighbor in parts[1:]]
            except ValueError:
                print(f"Invalid entry in line: {line}")
                continue  # Skip this line and move to the next one

            for neighbor_id in neighbors:
                graph.add_edge(unit_id, neighbor_id)

    return graph


import os 
# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)


if __name__ == "__main__":
    gal_file_path = "Lab04-1.gal"
    graph = create_graph_from_gal(gal_file_path)

    # Report summary statistics
    print(f"Average Connectivity: {graph.average_connectivity()}")
    max_conn, max_conn_nodes = graph.max_connectivity()
    print(f"Maximum Connectivity: {max_conn} (Node(s): {max_conn_nodes})")
    min_conn, min_conn_nodes = graph.min_connectivity()
    print(f"Minimum Connectivity: {min_conn} (Node(s): {min_conn_nodes})")
    disconnected = graph.disconnected_nodes()
    print(f"Disconnected Nodes: {disconnected or 'None'}")
