from typing import Iterable

INPUT_FILE = '2025/5_input.txt'


def find_answer(lines: Iterable[str]):
    fresh_id_ranges = []
    answer2 = 0

    for l in lines:
        l = l.strip()
        if not l:
            break

        cur_range = list(map(int, l.split('-')))

        i_ranges_to_remove = []
        for i, range in enumerate(fresh_id_ranges):
            if cur_range[0] > range[1] or cur_range[1] < range[0]:
                continue

            if cur_range[0] >= range[0] and cur_range[1] <= range[1]:
                cur_range = None
                break

            if cur_range[0] <= range[0] and cur_range[1] >= range[1]:
                i_ranges_to_remove.append(i)
                continue

            if cur_range[0] <= range[0] <= cur_range[1] <= range[1]:
                cur_range[1] = range[1]
                i_ranges_to_remove.append(i)
                continue

            if range[0] <= cur_range[0] <= range[1] <= cur_range[1]:
                cur_range[0] = range[0]
                i_ranges_to_remove.append(i)
                continue

        for i in reversed(i_ranges_to_remove):
            del fresh_id_ranges[i]

        if cur_range:
            fresh_id_ranges.append(cur_range)

    for b, e in fresh_id_ranges:
        answer2 += e - b + 1

    answer = 0
    for id in lines:
        id = int(id)
        for b, e in fresh_id_ranges:
            is_fresh = b <= id <= e
            if is_fresh:
                answer += 1
                break

    print(f'Answer is {answer}')
    print(f'Answer for part 2 is {answer2}')


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
