import pickle

t =  (1,2,"banana")

with open("pickle_file.pickle", "wb") as file:
    pickle.dump(t, file)

with open("pickle_file.pickle", "rb") as file:
    tup_load = pickle.load(file)
    print(tup_load)
