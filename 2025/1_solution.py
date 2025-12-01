from typing import Iterable

INPUT_FILE = '2025/1_input.txt'


def find_answer(lines: Iterable[str]):
    position = 50
    n_positions = 100

    answer_1 = 0
    answer_2 = 0

    print(f'The dial starts by pointing at {position}')

    for line in lines:
        direction = line[0]
        count = int(line[1:])

        old_position = position

        match direction:
            case 'L':
                position -= count
            case 'R':
                position += count

        n_crossings = abs(position // n_positions)
        position %= n_positions

        #                   div  rot  ans2
        # 50 -> R150 -> 0:   2    1   +2
        # 50 -> L150 -> 0:  -1    1   +2
        # 0 -> R150 -> 50:   1    1   +1
        # 0 -> L150 -> 50:  -2    1   +1
        if old_position == 0 and direction == 'L':
            n_crossings -= 1

        if position == 0 and direction == 'R':
            n_crossings -= 1

        answer_1 += position == 0
        answer_2 += (position == 0) + n_crossings

        message = f'The dial is rotated {line[:-1]} to point at {position}'
        if n_crossings > 0:
            message += f'; during this rotation, it points at 0 {n_crossings} time(s)'

        print(message)

    print(f'The answer for part 1 is {answer_1}')
    print(f'The answer for part 2 is {answer_2}')


with open(INPUT_FILE) as file:
    find_answer(file)
