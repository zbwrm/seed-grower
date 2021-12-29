import random

# set up tables
tech_levels = [["stone age", "bronze age", "medieval", "renaissance", "early industrial revolution"],
               [1, 2, 3, 2, 1]]

biomes = [["swamp", "hill", "mountain", "forest", "plains", "jungle", "desert", "aquatic"],
                     [1, 2, 2, 3, 3, 2, 2, 1]]

absurdities_list = ["lack of abstract thought", "no affection expressed or felt", "no distinctions made between different age grades (such as 'child', 'middle-aged', 'old')", "no religion", "no belief in fortune or misfortune", "biological and social mother are usually a different person", "abhorrence of body adornment", "no classification of colours", "no classification of flora or fauna", "no classification of kin", "no classification of weather conditions", "no classification of sex", "no conflict", "no cooking", "taboo against sex in private", "no cooperation", "absence of greetings", "absence of daily routine", "no distinction between right and wrong", "nocturnal", "no understanding that dreams are not reality", "lack of envy", "no etiquette rules", "no facial expressions", "no fear of death", "lack of figurative speech", "generosity considered weak", "lack of gift-giving", "absence of group living", "no attempts made to heal sick or injured", "no concept of imagery", "no rules concerning inheritance", "no concept of inheritance", "no concept of humour", "language is only a simply reflection of reality", "no concept of law", "no distinction made between general and particular", "women dominate public realm", "women more aggressive", "women more prone to lethal violence", "women more prone to theft", "no concept of meal times", "no concept of metaphor", "no prohibition of murder", "no numbers", "no personal names", "no concept of poetry", "no concept of music", "no concept of promising", "no concept of revenge", "extreme risk-aversion", "no concept of punishment", "lack of shame", "time only understood as cyclical", "no concept of trade", "language has no verbs", "language has no nouns", "no concept of weapons", "no death rituals", "no preference for one's own children or close kin"]
taboos_list = ["standing upwind of someone", "standing downwind of someone", "walking across somebody's path", "entering a building without explicit invitation from someone inside", "sitting down in company", "eating in public", "being seen while asleep", "contact with animals", "being in the shade", "being in direct sunlight", "particular colour", "direct speech between members of the same sex, age category, etc.", "eye contact", "discussing intentions or desires in public", "refusing requests", "stepping on anything living", "being touched by rain", "laughing", "being seen to be bleeding", "shouting", "standing in front of, behind, or beside somebody", "encountering any acquaintance without performing extended ritualistic pleasantries ", "being seen/heard to ask for, or accept, money", "being seen to be breathless, sweaty, or having otherwise striven in the performance of any task", "being visible through a window", "exposing one's hands, feet, nose, ears, etc.", "carrying anything in one's hands", "asking a direct question", "picking anything up off the ground", "whispering"]


mitigations_list = ["at certain times of day", "after performing a certain ritual", "while wearing something particular", "if performed by a particular type of person", "after making a donation"]

# generate values
tech_level = random.choices(tech_levels[0], tech_levels[1])

biome = random.choices(biomes[0], biomes[1])

number_of_absurdities = random.randint(1,3)
absurdities = random.choices(absurdities_list, k=number_of_absurdities)

number_of_taboos = random.randint(1,3)
taboos = random.choices(taboos_list, k=number_of_taboos)

number_of_mitigations = random.randint(0, number_of_taboos)
mitigations = random.choices(mitigations_list, k=number_of_mitigations)

# print values
print(f"Technology level: {tech_level}")
print(f"Biome:            {biome}")
print(f"Absurdities:      {absurdities}")
print(f"Taboos:           {taboos}")
print(f"Mitigations:      {mitigations}")