import sys
from collections import Counter


class outline:
    """
    class to take care of numbered bullet points
    """
    count = [0,0,0,0,0,0,0,0]

    def get_count(self):
        """
        forms number based on list, removes extra zeros
        :return: string: eg: 3.1.1
        """
        number = ''
        for num in self.count:
            if num is not 0:
                number += str(num) + '.'
        return number[:-1]

    def increment_count(self, modifier):
        """
        based on count of start it increments number in list and replaces higher position with Zeros
        :param modifier: text with '*'
        :return: None
        """
        counter = Counter(modifier)
        pos = counter['*']
        self.count[pos] += 1
        for i in range(len(self.count)):
            if i > pos:
                self.count[i] = 0


count = outline()
global_intented_list = []


def calculate_print_intend(line=None, printf=False):
    """
    Takes in text appends in list, when instucted to print prints the text with intend
    :param line: intended line with ... in front of them
    :param printf: to print or not
    :return: None
    """
    global global_intented_list
    if line:
        global_intented_list.append(line)
    if printf:
        prev_count = 1
        for i in range(0, len(global_intented_list)):
            prev_count = print_with_intend(global_intented_list, i, prev_count)
        global_intented_list = []


def get_intend_count(line):
    counter = Counter(line)
    return counter['.']


def print_with_intend(intented_list, pos, prev_count):
    """
    :param intented_list: list of text
    :param pos: position to print
    :return: prints text on stdout
    """
    symbol = '-'
    line = intented_list[pos]
    countx = get_intend_count(line)
    if not countx:
        countx = prev_count
        space = ' ' * (countx + 3)
        sys.stdout.write(space + line)
        return countx
    space = ' ' * (countx+1)
    next_count = 0
    if pos < len(intented_list)-1:
        next_count = get_intend_count(intented_list[pos+1])
    if next_count > countx:
        symbol = '+'
    line = line.replace('.', '')
    sys.stdout.write(space + symbol + line)
    return countx


def main():
    """
    read piped input to the program ad]nd parse it
    :return: None
    """
    previous_is_intended = False
    for line in sys.stdin:
        if line.startswith('*'):
            if previous_is_intended:
                previous_is_intended = False
                calculate_print_intend(None, True)
            count.increment_count(line)
            line = line.replace('*', '')
            sys.stdout.write(count.get_count()+line)
        elif line != '\n':
            previous_is_intended = True
            calculate_print_intend(line)


if __name__ == '__main__':
    main()
