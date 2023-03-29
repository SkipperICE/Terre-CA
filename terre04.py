import sys

start = ord(sys.argv[1])

for char in range(start, ord('z') + 1):
    print(chr(char), end='')
print()