import sys, datetime

file_name = sys.argv[1]
text = sys.argv[2]

with open(file_name, 'w') as f:
    f.write(text + '@' + str(datetime.datetime.now()))

#sys.exit(0)