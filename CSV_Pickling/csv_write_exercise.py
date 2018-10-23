from csv import reader, writer, DictWriter

fp = "/Users/tomtom/Documents/Modern Python 3 Bootcamp/CSV_Pickling"

# with open("/Users/tomtom/Documents/Modern Python 3 Bootcamp/CSV_Pickling/example_write.csv", "w") as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(["Marvin", "Slays"])

with open(fp + "/fighters.csv") as file:
    csv_reader = reader(file)
    with open("scream_fighters.csv", "w") as file:
        csv_writer = writer(file)
        for figher in csv_reader:
            csv_writer.writerow([s.upper() for s in figher])

with open("dictwriter_example.csv", "w") as file:
    headers = ["Name", "Dancer", "Age"]
    csv_writer = DictWriter(file, fieldnames = headers)
    csv_writer.writeheader()
    csv_writer.writerow({
            "Name" : "Michael",
            "Dancer" : "King of Pop",
            "Age" : "Way older for Neverland Ranch"
    })


''' Append to existing file '''

def add_user(first_name, last_name):
    with open(fp + "/fighters.csv", "a") as file:
        csv_writer = writer(file)
        csv_writer.writerow([first_name, last_name])

add_user("Dwayne", "Johnson")
