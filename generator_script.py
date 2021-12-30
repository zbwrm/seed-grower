import random
import argparse
from city.city import City

# TODO
"""
input variables
-l [filename] write to log
-v verbose
"""

parser = argparse.ArgumentParser(description='A random generator of cultural characteristics intended to spark ideas and help draw threads.')
parser.add_argument('-s', '--seed-directory', help='Sets the seed directory for the generator.', default='default',type=str)

args = parser.parse_args()

city = City(args.seed_directory)
city.read_from_tree()

print(city)