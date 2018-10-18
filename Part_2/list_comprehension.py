colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# списковое включение -> [x for some in list_some]
l_com = [(color, size) for color in colors for size in sizes]

print(l_com)
