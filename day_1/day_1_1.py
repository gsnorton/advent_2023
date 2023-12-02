#
# day_1_1.py
#

import fileinput
import re

def _main():
    for line in fileinput.input():
        if fileinput.isfirstline():
            _sum = 0

        _sum += int(''.join((line[re.search(r"\d", line).start()],
                             line[::-1][re.search(r"\d", line[::-1]).start()])))

    try:
        print(_sum)
    except UnboundLocalError:
        pass

if __name__ == '__main__':
    _main()
