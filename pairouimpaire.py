import sys

try:
    argument = int(sys.argv[1])

    if argument % 2 == 0:
        print(f"L'argument {argument} est pair")
    else:
        print(f"L'argument {argument} est impair")
        
except (IndexError, ValueError, SyntaxError, NameError):
    argument = sys.argv[1]
    print(f"L'argument en entree {argument} n'est pas n'est pas un nombre entier.")