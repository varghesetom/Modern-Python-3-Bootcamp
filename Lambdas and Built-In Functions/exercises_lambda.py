# Cube Lambda

cube = lambda x : x **3

# Map and Lambda

decrement_list = list(map(lambda x: x -1, [1,2,3]))

# Filter - Remove Negatives

def remove_negs(nums):
    return list(filter(lambda x: x>= 0, nums))

# All Exercise

def is_all_strings(lst):
    return all(type(l) == str for l in lst)

# Sorted

users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
sorted(users, key = lambda x : x["username"])
# Finding our most active users...
# Sort users by number of tweets, descending
tweeter = sorted(users,key=lambda user: len(user["tweets"]), reverse=True)


songs = [
	{"title": "happy birthday", "playcount": 1},
	{"title": "Survive", "playcount": 6},
	{"title": "YMCA", "playcount": 99},
	{"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
min(songs, key=lambda s: s['playcount']) #{"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title'] #YMCA



# Find the Max Magnitude
def max_magnitude(nums):
    return max(abs(num) for num in nums) #abs can't work on list itself, need to
                                         # call it on each element

# Find Sum of Even Values for Undetermined Number of Arguments
def sum_even_values(*args):
    evens = [x for x in args if x % 2 ==0]
    return sum(evens)

# Triple and Filter

def triple_and_filter(iters):
    div_4 = list(filter(lambda x : x % 4 == 0, iters))
    return [x*3 for x in div_4]

# OPTION 2

def triple_and_filter_2(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

# Extracting Full Names from a List of Dictionaries
def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))
