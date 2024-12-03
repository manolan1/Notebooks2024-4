import fileinput

with fileinput.input() as f:
    for line in f:
        print(line[:-1])