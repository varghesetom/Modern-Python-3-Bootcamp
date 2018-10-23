file = open("/Users/tomtom/Documents/Modern Python 3 Bootcamp/File IO/emps.txt")
print(file.read())
file.close()

## resets the seek cursor back to beginning if reading from terminal
# file.seek(0)

with open("/Users/tomtom/Documents/Modern Python 3 Bootcamp/File IO/emps.txt") as file:
    file.seek(0)
    file.read()

with open("shawty.txt", "w") as file:
    file.write("is a melody")
