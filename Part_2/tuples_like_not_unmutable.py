lax_coordinates = (33.5436654, -118.32543645)
city, year, pop, chg, area = ('Tokyo', 2018, 32450, 0.66, 8014)
travel_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

for passport in sorted(travel_ids):
    # operator % понимает кортежи и трактует каждый элемент как отдельное поле
    print('%s/%s' % passport)

for country, _ in sorted(travel_ids):
    print('%s' % country)


# tuple unpacking:
latitude, longitude = lax_coordinates   # параллельное присваивание
print(latitude)
print(longitude)

# i love this example (reverse without middle variable)
latitude, longitude = longitude, latitude
print(latitude)
print(longitude)

# unpacking with *
print(divmod(20, 8))

t = (20, 8)
print(divmod(*t))

quotient, remainder = divmod(*t)
print(quotient)
print(remainder, "\n")


# оператор для извлечение
a, *b, rest = range(5)
print(a)
print(b)
print(rest)
