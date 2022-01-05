#!/usr/bin/python3
"""Alta3 Research | RZFeeser
   Review of Lists and Dictionaries"""

# define a short data set (in real world, we want to read this from a file or API)
munsters = {'endDate': 1966, 'startDate': 1964,\
        'names':['Lily', 'Herman', 'Grandpa', 'Eddie', 'Marilyn']}   # {} creates dict

# Your solution goes below this line
# ----------------------------------
print("Names:", munsters['names'])
print("EndDate:", munsters['endDate'])
print("StartDate:", munsters["startDate"])
munsters["episodes"] = 70
print("Added episodes value is:", munsters['episodes'])
