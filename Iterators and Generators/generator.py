## Example of Generator

def week():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday",
    "Friday", "Saturday", "Sunday"]
    count = 0
    while count < len(days):
        yield days[count]
        count += 1

def yes_no():
    answer = "yes"
    while True:
        yield answer
        if answer == "yes":
            answer = "no"
        else:
            answer = "yes"

# gen = yes_no()
# print(next(gen))
# print(next(gen))

''' Generators are used to yield values one at a time '''

def current_beat():
    nums = (1,2,3,4)
    i = 0
    while True:
        if i >= len(nums): i = 0
        yield nums[i]
        i +=1

counter = current_beat()
print(next(counter))

''' Generators can also be useful for memory storage and time '''
def fib_gen(max):
    x, y = 0,1
    count = 0
    while count < max:
        x, y = y, x+y
        yield x
        count +=1


def get_multiple(num =1, count = 10):
    next_num = num
    while count > 0:
        yield next_num
        next_num += num

import time


# SUMMING 10,000,000 Digits With Generator Expression
gen_start_time = time.time() # save start time
print(sum(n for n in range(100000000)))
gen_time = time.time() - gen_start_time # end time - start time


# SUMMING 10,000,000 Digits With List Comprehension
list_start_time = time.time()
print(sum([n for n in range(100000000)]))
list_time = time.time() - list_start_time


print(f"sum(n for n in range(10000000)) took: {gen_time}")
print(f"sum([n for n in range(10000000)]) took: {list_time}")
