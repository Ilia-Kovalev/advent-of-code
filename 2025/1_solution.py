INPUT_FILE = '2025/1_input.txt'


class Dial:

    def __init__(self, *,
                 position: int = 50,
                 max: int = 99,
                 position_for_password: int = 0):
        self._position = position
        self._max = max
        self._position_for_password = position_for_password
        print(f'The dial starts by pointing at {self._position}')

    def rotate_left(self, count: int):
        self._position -= count
        self._position %= self._max + 1
        print(f'The dial is rotated L{count} to point at {self._position}')

    def rotate_right(self, count: int):
        self._position += count
        self._position %= self._max + 1
        print(f'The dial is rotated R{count} to point at {self._position}')

    @property
    def at_position_for_password(self) -> bool:
        return self._position == self._position_for_password


dial = Dial()

answer = 0

with open(INPUT_FILE) as file:
    for line in file:
        direction = line[0]
        count = int(line[1:])

        match direction:
            case 'L':
                dial.rotate_left(count)
            case 'R':
                dial.rotate_right(count)

        answer += dial.at_position_for_password

print(f'The answer is {answer}')
