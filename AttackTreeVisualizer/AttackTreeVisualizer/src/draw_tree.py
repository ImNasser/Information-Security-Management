import networkx as nx
import matplotlib.pyplot as plt

def draw_attack_tree(tree_data, parent_name, graph, pos=None, level=0, width=2., vert_gap = 0.4):
    if pos is None:
        pos = {parent_name: [0, 0]}
    else:
        pos[parent_name] = [pos[parent_name][0], pos[parent_name][1] - vert_gap]
    
    new_x = pos[parent_name][0] - width/2
    
    for child in tree_data.get('children', []):
        child_name = child['name']
        graph.add_node(child_name, value=child.get('value'))  # Adding child node with value if exists
        graph.add_edge(parent_name, child_name)  # Adding edge between parent and child
        
        new_x += width / (len(tree_data.get('children', [])) + 1)
        pos[child_name] = [new_x, level - vert_gap]
        
        draw_attack_tree(child, child_name, graph, pos, level - vert_gap, width / len(tree_data.get('children', [])), vert_gap)
    
    labels = {node: node + (" (" + str(data.get("value", "")) + ")" if data.get("value") else "") for node, data in graph.nodes(data=True)}
    nx.draw(graph, pos=pos, labels=labels, with_labels=True)

