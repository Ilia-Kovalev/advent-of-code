from typing import Iterable
from functools import reduce
import operator

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

    connections = []
    while len(connections) < n_connections:
        idx_shortest = min(range(len(distances)), key=lambda i: distances[i])
        i_shortest = idx_shortest // len(points)
        j_shortest = idx_shortest % len(points)
        connections.append((i_shortest, j_shortest))
        distances[idx_shortest] = float('inf')
        print(f'{len(connections)} / {n_connections}')

    circuits = []
    while connections:
        boxes = set(connections.pop())
        i_found = []
        for i, c in enumerate(circuits):
            if boxes & c:
                c |= boxes
                i_found.append(i)

        if not i_found:
            circuits.append(boxes)

        if len(i_found) == 2:
            circuits[i_found[0]] |= circuits[i_found[1]]
            del circuits[i_found[1]]

    answer = reduce(operator.mul, map(len, sorted(
        circuits, key=len, reverse=True)[:3]), 1)
    print(f'Answer is {answer}')


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
