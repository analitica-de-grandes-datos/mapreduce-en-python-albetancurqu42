#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#

import sys

if __name__ == '__main__':

    dict_letters = {}

    for line in sys.stdin:

        value, letters = line.split("\t")
        value = int(value)

        letters = letters.strip().split(',')

        for ll in letters:

            if ll not in dict_letters.keys():
                dict_letters[ll] = []

            dict_letters[ll].append(value)

    for key in sorted(dict_letters.keys()):

        letters_list = ",".join([str(ii) for ii in sorted(dict_letters[key])])

        sys.stdout.write(f'{key}\t{letters_list}\n')
