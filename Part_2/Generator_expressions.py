from array import array

# генераторное выражение -> (x for x in some)
symbols = '$6£¥€п'
genexp_tuple = tuple(ord(symbol) for symbol in symbols)

print(genexp_tuple)

genexp_array = array('I', (ord(symbol) for symbol in symbols))
print(genexp_array)


colors = ['white', 'black']
sizes = ['S', 'L', 'L']

for tshirt in ('{} {}'.format(c, s) for c in colors for s in sizes):
    print(tshirt)

