import pandas as pd
from functools import reduce
from os import listdir, path
import random

# define Quality class
class Quality:
    """
    Defines a given cultural, geographic, or other quality of the city.
    """

    def __init__(self, name, tag, seed):
        """
        Reads a list of options from a given CSV file in the same directory.
        """
        self.data = pd.read_csv(path.join(seed, tag, name.replace(' ', '_')+'.csv'),index_col=False)
        self.options = self.data[1::]
        self.tag = tag
        self.seed = seed
        self.amount_lower = int(list(self.data.loc[0])[0].split()[1])
        self.amount_upper = int(list(self.data.loc[0])[0].split()[1])
        self.last_sample_size = None
        self.name = name
    
    def sample(self):
        """
        Samples amount options from self.options.
        """
        self.last_sample_size = random.randint(self.amount_lower, self.amount_upper)
        return reduce(lambda a,b:a+b, self.options.sample(self.last_sample_size).values.tolist())
    
    def __format__(self, __format_spec: str) -> str:
        return f"{len(self.options)} options for {self.name}"

class City:
    """
    Holds and organizes a bunch of qualities together.
    """
    def __init__(self, seed_directory):
        self.qualities = {}
        self.seed_directory = seed_directory
    def add_quality(self, quality):
        if quality.tag in self.qualities.keys():
            self.qualities[quality.tag].append(quality)
        else:
            self.qualities[quality.tag] = [quality]
    
    def add_tag(self, tag):
        self.qualities[tag] = []

    def new_quality(self, name, tag, seed):
        self.add_quality(Quality(name, tag, seed))

    def read_from_tree(self):
        seed = path.join('seeds',self.seed_directory)
        for tag in listdir(seed):
            if '.' in tag:
                continue
            self.add_tag(tag)
            for quality_file in listdir(path.join(seed,tag)):
                if 'DS' in quality_file:
                    continue
                name = quality_file[:-4].replace('_', ' ')
                self.new_quality(name, tag, seed)

    def __str__(self) -> str:
        format_string = ""
        for tag in self.qualities:
            format_string += f"\n\n{tag}"
            for quality in self.qualities[tag]:
                format_string += f"\n- {quality.name}"
                for selection in quality.sample():
                    format_string += f"\n  - {selection}"
        return format_string