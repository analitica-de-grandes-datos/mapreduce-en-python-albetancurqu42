#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from copy import copy

if __name__ == '__main__':

    curkey = None
    list_vals = []

    for aux, line in enumerate(sys.stdin):
        key, val, date = line.split("\t")
        date = date.strip()
        val = int(val)

        if curkey is None:
            curkey = copy(key)

        if curkey != key:

            sys.stdout.write(f"{curkey}	{sum(list_vals)}	{sum(list_vals)/len(list_vals)}\n")

            list_vals = []
            list_vals.append(val)

            curkey = copy(key)
        else:
            list_vals.append(val)

    sys.stdout.write(f"{curkey}	{sum(list_vals)}	{sum(list_vals)/len(list_vals)}\n")
