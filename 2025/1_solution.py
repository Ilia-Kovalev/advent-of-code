INPUT_FILE = '2025/1_input.txt'


class Dial:

    def __init__(self, *,
                 position: int = 50,
                 n_positions: int = 100,
                 position_for_password: int = 0):
        self._position = position
        self._n_positions = n_positions
        self._position_for_password = position_for_password
        self._n_stops_at_position_for_password = 0
        print(f'The dial starts by pointing at {self._position}')

    def rotate_left(self, count: int):
        self._position -= count
        self._normalize_position()
        self._n_stops_at_position_for_password += self._at_password_position
        print(f'The dial is rotated L{count} to point at {self._position}')

    def rotate_right(self, count: int):
        self._position += count
        self._normalize_position()
        self._n_stops_at_position_for_password += self._at_password_position
        print(f'The dial is rotated R{count} to point at {self._position}')

    @property
    def password(self) -> int:
        return self._n_stops_at_position_for_password

    def _normalize_position(self):
        self._position %= self._n_positions

    @property
    def _at_password_position(self) -> bool:
        return self._position == self._position_for_password


dial = Dial()

with open(INPUT_FILE) as file:
    for line in file:
        direction = line[0]
        count = int(line[1:])

        match direction:
            case 'L':
                dial.rotate_left(count)
            case 'R':
                dial.rotate_right(count)

print(f'The answer is {dial.password}')
