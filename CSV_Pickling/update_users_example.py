import csv

## 1. Updating Users 

def update_users(oldfn, oldln, newfn, newln):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    count = 0
    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == oldfn and row[1] == oldln:
                csv_writer.writerow([newfn, newln])
                count +=1
            else:
                csv_writer.writerow(row)

    return "Users updated: {}".format(count)

## 2 . Deleting Users

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

def delete_users(oldfn, oldln):
    with open("users.csv") as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    count = 0

    with open("users.csv", "w") as file:
        csv_writer = csv.writer(file)
        for row in rows:
            if row[0] == oldfn and row[1] == oldln:
                del row
                count +=1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}.".format(count)
