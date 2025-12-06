from typing import Iterable
from functools import reduce
import operator

INPUT_FILE = '2025/6_input.txt'

def parse(line: str):
    return filter(bool, line.strip().split(' '))

def find_answer(lines: Iterable[str]):
    answer = 0

    first_line = list(parse(next(lines)))
    problems = [[number] for number in first_line]

    for line in lines:
        for i, number in enumerate(parse(line)):
            problems[i].append(number)
    
    for problem in problems:
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
        find_answer(f)
else:
    find_answer(EXAMPLE)
