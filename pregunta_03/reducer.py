#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

if __name__ == "__main__":
    for line in sys.stdin:

        content = line.split(",")

        sys.stdout.write(f'{content[1].strip()},{content[0]}\n')
