from typing import Iterable
from functools import reduce
import operator
import numpy as np

INPUT_FILE = '2025/8_input.txt'


def find_answer(lines: Iterable[str], n_connections):
    points = tuple(map(lambda x: tuple(map(int, x.split(','))), lines))
    distances = []
    for i, p1 in enumerate(points):
        for j, p2 in enumerate(points):
            if j <= i:
                distances.append(float('inf'))
            else:
                distances.append(
                    sum(map(lambda ps: (ps[0] - ps[1]) ** 2, zip(p1, p2))))

    circuits = [{i} for i in range(len(points))]
    n_connected = 0
    last_connected = None
    n_possible_connections = sum(x < float('inf') for x in distances)
    distances = np.array(distances)
    while n_connected < n_possible_connections:
        idx_shortest = distances.argmin()
        i_shortest = idx_shortest // len(points)
        j_shortest = idx_shortest % len(points)
        distances[idx_shortest] = float('inf')
        print(f'{n_connected} / {n_possible_connections}')
        boxes = {i_shortest, j_shortest}

        # print(points[i_shortest], points[j_shortest])

        i_found = []
        already_connected = False
        for i, c in enumerate(circuits):
            if not boxes - c:
                already_connected = True
                break

            if boxes & c:
                c |= boxes
                i_found.append(i)

        if len(i_found) == 2:
            circuits[i_found[0]] |= circuits[i_found[1]]
            del circuits[i_found[1]]

        if not already_connected:
            last_connected = boxes

        n_connected += 1

        if n_connected == n_connections:
            answer = reduce(operator.mul, map(len, sorted(
                circuits, key=len, reverse=True)[:3]), 1)

    i1, i2 = last_connected
    answer2 = points[i1][0] * points[i2][0]
    print(f'Answer is {answer}')
    print(f'Answer2 is {answer2}')


EXAMPLE = iter('''
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
'''[1:-1].split('\n'))

if True:
    with open(INPUT_FILE) as f:
        find_answer(f, 1000)
else:
    find_answer(EXAMPLE, 10)
