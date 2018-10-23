class GrumpyDict(dict):
	def __repr__(self):
		print("NONE OF YOUR BUSINESS")
		return super().__repr__()  ## calling in the normal dictionary __repr__

	def __missing__(self, key):
		print(f"YOU WANT {key}?  WELL IT AINT HERE!")

	def __setitem__(self, key, value):
		print("YOU WANT TO CHANGE THE DICTIONARY?")
		print("OK FINE...")
		super().__setitem__(key, value) ## can research online to find out the
                                        ## specific dictionary dunder methods

	def __contains__(self, item):
		print("NO IT AINT IN HERE!")
		return True

# data = GrumpyDict({"first": "Tom", "animal": "lion"})
# print(data)
# data['city'] = 'Tokyo'
# print(data)
# "city" in data
#
#
# if 'city' in data.keys():
#     print("YOOOOO")
#

class Train:

    def __init__(self, num):
        self.num_cars = num

    def __repr__(self):
        print(f"{self.num_cars} car train")

    def __len__(self):
        return {self.num_cars}
