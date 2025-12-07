from typing import Iterable

INPUT_FILE = '2025/7_input.txt'


def find_answer(lines: Iterable[str]):
    first_line = next(lines)

    n_splits = 0
    beam_poss = {first_line.index('S'): 1}

    for line in lines:
        new_beam_poss = {}
        for pos, n_timelines in beam_poss.items():
            match line[pos]:
                case '.':
                    new_poss = [pos]
                case '^':
                    new_poss = pos - 1, pos + 1
                    n_splits += 1

            for new_pos in new_poss:
                if new_pos in new_beam_poss:
                    new_beam_poss[new_pos] += n_timelines
                else:
                    new_beam_poss[new_pos] = n_timelines

        beam_poss = new_beam_poss

        vals = tuple(map(str, beam_poss.values()))
        max_val_len = max(map(len, vals))
        vals = [v.zfill(max_val_len) for v in vals]
        message = [line] * max_val_len
        for pos, val in zip(beam_poss, vals):
            for i, c in enumerate(val):
                m = message[i]
                message[i] = m[:pos] + c + m[pos+1:]

        print('\n'.join(message), end=': ')
        print(sum(beam_poss.values()))

    print(f'Answer is {n_splits}')
    print(f'Answer 2 is {sum(beam_poss.values())}')


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
