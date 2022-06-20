#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey = None
    val_max = 0
    val_min = 0

    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
            val_max = max(val_max, val)
            val_min = min(val_min, val)
        else:

            if curkey is not None:
                sys.stdout.write(f"{curkey}\t{val_max}\t{val_min}\n")

            curkey = key
            val_max = val
            val_min = val

    sys.stdout.write(f"{curkey}\t{val_max}\t{val_min}\n")