def format_stylish(diff, depth=0):
    lines = []
    indent = ' ' * (depth * 4)
    
    for node in diff:
        key = node['key']
        node_type = node['type']
        
        if node_type == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif node_type == 'unchanged':
            formatted_value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {formatted_value}")
        elif node_type == 'added':
            formatted_value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {formatted_value}")
        elif node_type == 'removed':
            formatted_value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {formatted_value}")
        elif node_type == 'changed':
            old_formatted = format_value(node['old_value'], depth + 1)
            new_formatted = format_value(node['new_value'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_formatted}")
            lines.append(f"{indent}  + {key}: {new_formatted}")
    
    if depth == 0:
        lines.insert(0, '{')
        lines.append('}')
    
    return '\n'.join(lines)


def format_value(value, depth):
    if value == '':
        return ''  # Особый случай для пустой строки
    
    if isinstance(value, dict):
        if not value:  # Пустой словарь
            return '{}'
            
        indent = ' ' * (depth * 4)
        lines = ['{']
        for key, val in value.items():
            formatted_val = format_value(val, depth + 1)
            lines.append(f"{indent}    {key}: {formatted_val}")
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return value
    else:
        return str(value)