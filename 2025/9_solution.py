from typing import Iterable

import numpy as np

INPUT_FILE = '2025/9_input.txt'


def find_answer(lines: Iterable[str], part2=False):
    points = np.array([tuple(map(int, l.split(','))) for l in lines])
    points[:, 0] -= points[:, 0].min()
    points[:, 1] -= points[:, 1].min()

    borders = np.zeros(points.max(axis=0) + 1, dtype=np.bool)

    for i in range(points.shape[0]):
        j = i + 1

        if j == points.shape[0]:
            j = 0

        p1, p2 = points[[i, j], :]
        if p1[0] == p2[0]:
            if p1[1] > p2[1]:
                p1, p2 = p2, p1

            borders[p1[0], p1[1]:p2[1]+1] = True
        else:
            if p1[0] > p2[0]:
                p1, p2 = p2, p1

            borders[p1[0]:p2[0]+1, p1[1]] = True

    squares = np.array([], int)
    all_i = np.array([], int)
    all_j = np.array([], int)
    for i in range(len(points) - 1):
        jj = np.array(range(i, len(points)))

        p1 = points[i, :]
        p2 = points[jj, :]

        new_squares = np.prod(np.abs(p1 - p2) + 1, axis=1)
        squares = np.concat([squares, new_squares])
        all_i = np.concat([all_i, [i] * len(jj)])
        all_j = np.concat([all_j, jj])

    ii = np.argsort(squares)[::-1]
    squares = squares[ii]
    all_i = all_i[ii]
    all_j = all_j[ii]

    i_max = 0

    if part2:
        for i, (i_p1, i_p2) in enumerate(zip(all_i, all_j)):
            p1 = points[i_p1, :]
            p2 = points[i_p2, :]

            print(i, p1, p2, squares[i])

            tl = (min(p1[0], p2[0]) + 1, min([p1[1], p2[1]]) + 1)
            br = (max(p1[0], p2[0]) - 1, max([p1[1], p2[1]]) - 1)

            if np.any(borders[tl[0], tl[1]:br[1]+1]):
                continue

            if np.any(borders[br[0], tl[1]:br[1]+1]):
                continue

            if np.any(borders[tl[0]:br[0]+1, tl[1]]):
                continue

            if np.any(borders[tl[0]:br[0]+1, br[1]]):
                continue

            if np.any(borders[tl[0]:br[0] + 1, tl[1]:br[1]+1]):
                continue

            i_max = i
            break

    print(f'Answer is {squares[i_max]}')

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
        find_answer(f, part2=True)
else:
    find_answer(EXAMPLE, part2=True)
