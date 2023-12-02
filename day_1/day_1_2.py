#
# day_1_2.py
#

import fileinput
import re

def _main():
    for line in fileinput.input():

        print(line.replace("one", '1').
                   replace("two", '2').
                   replace("three", '3').
                   replace("four", '4').
                   replace("five", '5').
                   replace("six", '6').
                   replace("seven", '7').
                   replace("eight", '8').
                   replace("nine", '9'))
        continue

        if fileinput.isfirstline():
            try:
                print(_sum)
            except UnboundLocalError:
                pass

            _sum = 0

        _sum += int(''.join((line[re.search(r"\d", line).start()],
                             line[::-1][re.search(r"\d", line[::-1]).start()])))

    try:
        print(_sum)
    except UnboundLocalError:
        pass

if __name__ == '__main__':
    _main()
