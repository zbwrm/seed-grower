import random
import pandas as pd
from functools import reduce

# set up tables
biomes_list = pd.read_csv("lists/biomes.csv",index_col=False)
absurdities_list = pd.read_csv("lists/absurdities.csv",index_col=False)
taboos_list = pd.read_csv("lists/taboos.csv",index_col=False)
mitigations_list = pd.read_csv("lists/mitigations.csv",index_col=False)

# pick numbers of stuff
biomes_number = random.choice([1, 1, 1, 1, 2])
absurdities_number = random.randint(1,3)
taboos_number = 4 - absurdities_number
mitigations_number = random.randint(1, taboos_number)

# generate values
biomes = reduce(lambda a,b:a+b, biomes_list.sample(biomes_number).values.tolist())
absurdities = reduce(lambda a,b:a+b, absurdities_list.sample(absurdities_number).values.tolist())
taboos = reduce(lambda a,b:a+b, taboos_list.sample(taboos_number).values.tolist())
mitigations = reduce(lambda a,b:a+b, mitigations_list.sample(mitigations_number).values.tolist())

# print values
print(f"Biome:       {biomes}")
print(f"Absurdities: {absurdities}")
print(f"Taboos:      {taboos}")
print(f"Mitigations: {mitigations}")

