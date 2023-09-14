def aggregate_values(node):
    if 'children' in node and len(node['children']) > 0:
        node['value'] = 0
        for child in node['children']:
            aggregate_values(child)
            node['value'] += child['value']
