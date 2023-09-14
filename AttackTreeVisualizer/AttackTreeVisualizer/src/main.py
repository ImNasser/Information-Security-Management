import networkx as nx
import matplotlib.pyplot as plt
from load_data import load_attack_tree
from draw_tree import draw_attack_tree
from user_input import add_values_to_leaf
from aggregate_values import aggregate_values

def main():
    # Step 1: Load Data
    file_path = "../data/attack_tree.json"
    attack_tree = load_attack_tree(file_path)
    
    while True:  # Loop to allow repeated updates
        # Step 2: Draw Initial Attack Tree
        G = nx.DiGraph()
        G.add_node(attack_tree['root']['name'])
        draw_attack_tree(attack_tree['root'], attack_tree['root']['name'], G)
        plt.pause(1)  # Pause to view the figure
        plt.clf()  # Clear the current figure
        
        # Step 3: Add User Values
        add_values_to_leaf(attack_tree['root'])
        
        # Step 4: Aggregate Values
        aggregate_values(attack_tree['root'])
        
        # Step 5: Draw Final Attack Tree
        G = nx.DiGraph()
        G.add_node(attack_tree['root']['name'])
        draw_attack_tree(attack_tree['root'], attack_tree['root']['name'], G)
        plt.pause(1)  # Pause to view the figure
        plt.clf()  # Clear the current figure

        # Ask user if they want to continue updating values
        user_input = input('Would you like to update values again? (y/n): ')
        if user_input.lower() == 'n':
            break

if __name__ == "__main__":
    main()
