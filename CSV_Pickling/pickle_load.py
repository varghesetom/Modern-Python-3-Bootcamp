### Python serialiazation --

## can convert python object into character stream so can reconstruct
## object in a completely separate file (will need additional instructions
## if there is Class information in order to fully reconstruct the object)


import pickle

with open("pickle_file.pickle", "rb") as file:
    tup_load = pickle.load(file)
    print(tup_load)
