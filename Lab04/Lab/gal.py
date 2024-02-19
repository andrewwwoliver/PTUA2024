class GALProcessor:
    def __init__(self, gal_dict):
        self.gal_dict = gal_dict

    def get_neighbor_dictionary(self):
        return {unit_id: list(neighbors) for unit_id, neighbors in self.gal_dict.items()}

    def get_neighbor_histogram(self):
        neighbor_histogram = {}
        for unit_id, neighbors in self.gal_dict.items():
            neighbor_count = len(neighbors)
            neighbor_histogram.setdefault(neighbor_count, []).append(unit_id)
        return neighbor_histogram

    def check_asymmetry(self):
        for unit_id, neighbors in self.gal_dict.items():
            if any(unit_id not in self.gal_dict.get(neighbor_id, []) for neighbor_id in neighbors):
                return True
        return False
    
    def get_neighbors_by_id(self, unit_id):
        """
        Get the neighbors of a spatial unit by its ID.

        Parameters:
        - unit_id: The ID of the spatial unit.

        Returns:
        - A list of neighbor IDs.
        """
        return list(self.gal_dict.get(unit_id, []))
    


def read_gal_file(file_path):
    gal_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split()
            unit_id = int(parts[0])

            try:
                neighbors = [int(neighbor) for neighbor in parts[1:]]
            except ValueError:
                print(f"Invalid entry in line: {line}")
                continue

            gal_dict[unit_id] = neighbors

    return gal_dict

import os

# Get the absolute path to the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Change the working directory to the script's directory
os.chdir(script_dir)

if __name__ == "__main__":
    # Specify the path to Lab04-1.gal
    gal_file_path = "Lab04-1.gal"

    # Read the GAL file
    gal_data = read_gal_file(gal_file_path)

    # Create GALProcessor instance
    gal_processor = GALProcessor(gal_data)

    # 1. Get neighbor dictionary
    neighbor_dict = gal_processor.get_neighbor_dictionary()
    print("Neighbor Dictionary:")
    print(neighbor_dict)

    # 2. Get neighbor histogram
    neighbor_histogram = gal_processor.get_neighbor_histogram()
    print("\nNeighbor Histogram:")
    print(neighbor_histogram)

    # 3. Check asymmetry
    asymmetry_exists = gal_processor.check_asymmetry()
    print("\nAsymmetry Exists:", asymmetry_exists)
     
    unit_id_to_check = 40
    neighbors_of_unit = gal_processor.get_neighbors_by_id(unit_id_to_check)
    print(f"\nNeighbors of Spatial Unit {unit_id_to_check}: {neighbors_of_unit}")
