def copy(file_name, file_name_copy):
    with open(file_name) as file:
        file.seek(0)
        text = file.read()

    with open(file_name_copy, "w") as new_file:
        new_file.write(text)


''' Note: to write the reversed use the [::-1] slicing on text

    i.e.  "new_file.write(text[::-1])"
'''

### Getting statistics

def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return {"lines" : len(lines),
            "words" : sum(len(line.split(" ")) for line in lines)
            "characters" : sum(len(line) for line in lines)
    }


### Replacing a word with all the new instances

def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
