from typing import Iterable

INPUT_FILE = '2025/5_input.txt'


def find_answer(lines: Iterable[str]):    
    fresh_id_ranges = []
 
    for l in lines:
        l = l.strip()
        if not l:
            break

        fresh_id_ranges.append(tuple(map(int, l.split('-'))))

    answer = 0
    for id in lines:
        id = int(id)
        for b, e in fresh_id_ranges:
            is_fresh = b <= id <= e
            if is_fresh:
                answer += 1
                break

    print(f'Answer is {answer}')


EXAMPLE = iter('''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''[1:-1].split('\n'))

if True:
    with open(INPUT_FILE) as f:
        find_answer(f)
else:
    find_answer(EXAMPLE)
