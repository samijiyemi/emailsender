import sys

if len(sys.argv) == 1:
    print("USAGE: python index.py <password>")
else:
    password = sys.argv[1]
    print("Password:", password)
