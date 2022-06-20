#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
from copy import copy

if __name__ == '__main__':

    list_vals = []

    for aux, line in enumerate(sys.stdin):
        key, val, date = line.split("\t")
        date = date.strip()
        val = int(val)

        list_vals.append((val, key, date))
        list_vals = sorted(list_vals)[:6]

    for (val, key, date) in list_vals:
        sys.stdout.write(f"{key}   {date}   {val}\n")
