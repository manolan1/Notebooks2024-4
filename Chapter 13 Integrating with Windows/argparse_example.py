import argparse

parser = argparse.ArgumentParser(
    prog='program_name',
    description='brief description',
    epilog='at the bottom of help')

parser.add_argument('filename')      # positional
parser.add_argument('-c', '--count') # takes a value

args = parser.parse_args()
print(args.filename, args.count)
