from collections import namedtuple

City = namedtuple('City', 'name country')
# tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))

names = [
    ('Kiev', 'UA'),
    ('New-York', 'US'),
    ('San Paolo', 'MX'),
    ('San-Fransisco', 'US')
]

for name, country in names:
    print(City(name, country))


def factorial(n):
    """
    :param n:
    :return: factorial from n
    """
    return 1 if n < 2 else n * factorial(n-1)


print(factorial(5))
print(type(factorial))
print(factorial.__doc__)

