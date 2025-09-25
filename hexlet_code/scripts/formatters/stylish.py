def format_velue(value, depth):
    if isinstance(value, dict):
        indent = '    ' * depth
        lines = ['{']
        for key, val in value.items():
            formatted_val = format_velue(val, depth + 1)
            lines.append(f"{indent}    {key}: {formatted_val})")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    else:
        return str(value)


def format_stylish(diff, depth=0):
    lines = []
    indent = '    ' * depth

    for node in diff:
        key = node['key']
        node_type = node['type']

        if node_type == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif node_type == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")
        elif node_type == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif node_type == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif node_type == 'changed':
            old_value = format_value(node['old_value'], depth + 1)
            new_value = format_value(node['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
    
    return '\n'.join(lines)
