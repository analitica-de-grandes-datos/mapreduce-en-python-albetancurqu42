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
            list_vals = sorted(list_vals, key=lambda tup: tup[0])

            for (val_sort, date_sort) in list_vals:
                sys.stdout.write(f"{curkey}\t{date_sort}\t{val_sort}\n")

            list_vals = []
            list_vals.append((val, date))

            curkey = copy(key)
        else:
            list_vals.append((val, date))

    list_vals = sorted(list_vals, key=lambda tup: tup[0])
    for (val_sort, date_sort) in list_vals:
        sys.stdout.write(f"{curkey}\t{date_sort}\t{val_sort}\n")
        






