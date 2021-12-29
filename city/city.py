import pandas as pd
from functools import reduce
import os

# define constants
LIST_LOCATION = "./lists"

# define Quality class
class Quality:
    """
    Defines a given cultural, geographic, or other quality of the city.
    """

    def __init__(self, name, tag, amount):
        """
        Reads a list of options from a given CSV file.
        """
        self.options = pd.read_csv(os.path.join(LIST_LOCATION, name.replace(' ', '_')+'.csv'),index_col=False)
        self.tag = tag
        self.amount = amount
        self.name = name
    
    def sample(self):
        """
        Samples amount options from self.options.
        """
        return reduce(lambda a,b:a+b, self.options.sample(self.amount).values.tolist())
    
    def __format__(self, __format_spec: str) -> str:
        return f"{len(self.options)} options for {self.name}"

class City:
    """
    Holds and organizes a bunch of qualities together.
    """
    def __init__(self):
        self.qualities = {}

    def add_quality(self, quality):
        if quality.tag in self.qualities.keys():
            self.qualities[quality.tag].append(quality)
        else:
            self.qualities[quality.tag] = [quality]
    
    def new_quality(self, name, tag, amount):
        temp_quality = Quality(name, tag, amount)
        self.add_quality(temp_quality)

    def __str__(self) -> str:
        format_string = ""
        for tag in self.qualities:
            format_string += f"\n{tag}"
            for quality in self.qualities[tag]:
                format_string += f"\n {quality.name}"
                for selection in quality.sample():
                    format_string += f"\n  {selection}"
        return format_string