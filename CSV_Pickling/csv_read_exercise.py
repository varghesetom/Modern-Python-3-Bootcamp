'''
    csv common file format for tabular data
'''

from csv import reader

fp = "/Users/tomtom/Documents/Modern Python 3 Bootcamp/CSV_Pickling/"

# with open(fp + "fighters.csv") as file:
#     csv_reader = reader(file)
#     next(csv_reader) ## skips the header row
#
#
#     ## Gives the data in a list of lists format
#     data = list(csv_reader)
#     for line in csv_reader:
#     	print(line)

# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open(fp + "fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data
