import random
from city.city import City


city = City()

city.new_quality('quirks', 'culture', random.randint(1,3))
city.new_quality('taboos', 'culture', random.randint(1,3))
city.new_quality('mitigations', 'culture', random.randint(1,2))

city.new_quality('biomes', 'geography', random.choice([1, 1, 1, 1, 2]))

city.new_quality('building styles', 'architecture', random.randint(2,4))
city.new_quality('building materials', 'architecture', random.randint(1,3))

print(city)
