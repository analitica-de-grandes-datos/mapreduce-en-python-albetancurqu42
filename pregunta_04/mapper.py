#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    for line in sys.stdin:

        content = line.split('   ')

        sys.stdout.write(f'{content[0]}\t1\n')
