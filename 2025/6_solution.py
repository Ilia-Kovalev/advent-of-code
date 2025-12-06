from typing import Iterable
from functools import reduce
import operator

INPUT_FILE = '2025/6_input.txt'

def parse(line: str):
    return filter(bool, line.strip().split(' '))


def parse_problems(lines: Iterable[str]):
    first_line = list(parse(next(lines)))
    problems = [[number] for number in first_line]

    for line in lines:
        for i, number in enumerate(parse(line)):
            problems[i].append(number)

    return problems


def parse_problems2(lines: Iterable[str]):
    lines = [l.replace('\n', '') for l in lines]
    columns = (''.join(line[i] for line in lines).replace(' ', '')
               for i in range(len(lines[0])))
    columns = filter(bool, columns)

    column = next(columns)
    current_sign = column[-1]
    problems = [[column[:-1]]]
    for column in columns:
        if column[-1] == '*' or column[-1] == '+':
            problems[-1].append(current_sign)
            problems.append([column[:-1]])
            current_sign = column[-1]
        else:
            problems[-1].append(column)

    problems[-1].append(current_sign)

    return problems


def find_answer(lines: Iterable[str], part2=False):
    answer = 0

    parser = parse_problems2 if part2 else parse_problems

    for problem in parser(lines):
        op = operator.add if problem[-1] == '+' else operator.mul
        out = reduce(op, map(int, problem[:-1]))
        print(f'{problem} = {out}')
        answer += out

    print(f'Answer is {answer}')


EXAMPLE = iter('''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
'''[1:-1].split('\n'))

if True:
    with open(INPUT_FILE) as f:
        find_answer(f, part2=True)
else:
    find_answer(EXAMPLE, part2=True)
