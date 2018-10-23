# loop through numbers 1-20 and
#  if x = 4,13 -> x is unlucky
# if x is even or odd, say so

for x in range(20):
    if (x == 4) or (x == 13):
        print(f"{x} is unlucky")
    elif (x % 2 == 0):
        print(f"{x} is even")
    else:
        print(f"{x} is odd")
