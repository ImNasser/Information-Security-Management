def add_values_to_leaf(node):
    if 'children' in node and len(node['children']) > 0:
        for child in node['children']:
            add_values_to_leaf(child)
    else:
        value = input(f"Enter the value for {node['name']}: ")
        node['value'] = int(value)
