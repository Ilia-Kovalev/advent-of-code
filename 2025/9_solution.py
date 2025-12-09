from typing import Iterable


INPUT_FILE = '2025/9_input.txt'


def find_answer(lines: Iterable[str]):
    points = [tuple(map(int, l.split(','))) for l in lines]
    
    max_square = 0
    for i in range(len(points) - 1):
        for j in range(i, len(points)):
            p1 = points[i]
            p2 = points[j]
            max_square = max((abs(p2[0] - p1[0]) + 1) * (abs(p2[1] - p1[1]) + 1), max_square)

    print(f'Answer is {max_square}')

EXAMPLE = iter('''
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
'''[1:-1].split('\n'))

if True:
    with open(INPUT_FILE) as f:
        find_answer(f)
else:
    find_answer(EXAMPLE)
