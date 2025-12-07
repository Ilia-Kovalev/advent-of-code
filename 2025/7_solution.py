from typing import Iterable

INPUT_FILE = '2025/7_input.txt'


def find_answer(lines: Iterable[str]):
    first_line = next(lines)

    n_splits = 0
    beam_poss = set([first_line.index('S')])

    for line in lines:
        new_beam_poss = set()

        for pos in beam_poss:
            match line[pos]:
                case '.':
                    new_beam_poss.add(pos)
                case '^':
                    new_beam_poss.update([pos - 1, pos + 1])
                    n_splits += 1

        beam_poss = new_beam_poss

    print(f'Answer is {n_splits}')


EXAMPLE = iter('''
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
'''[1:-1].split('\n'))

if True:
    with open(INPUT_FILE) as f:
        find_answer(f)
else:
    find_answer(EXAMPLE)
