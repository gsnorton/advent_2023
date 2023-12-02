#
# day_1_2.py
#

import fileinput
import re

# -----------------------------------------------------------------------------

def replace_words_digits(line):
    try:
        _m = re.search(r"one|two|three|four|five|six|seven|eight|nine", line)

        return replace_words_digits(line[:_m.start()] +
                                        _m.group().
                                        replace("one", '1').
                                        replace("two", '2').
                                        replace("three", '3').
                                        replace("four", '4').
                                        replace("five", '5').
                                        replace("six", '6').
                                        replace("seven", '7').
                                        replace("eight", '8').
                                        replace("nine", '9')
                                            + line[_m.end():])

    except AttributeError:
        return line

def _main():
    for _line in fileinput.input():
        if fileinput.isfirstline():
            _sum = 0

        line = replace_words_digits(_line)
        value = int(''.join((line[re.search(r"\d", line).start()],
                             line[::-1][re.search(r"\d", line[::-1]).start()])))
        _sum += value

        print(_line.strip(), line.strip(), value)

    try:
        print(_sum)
    except UnboundLocalError:
        pass

if __name__ == '__main__':
    _main()
