from typing import Iterable

INPUT_FILE = '2025/4_input.txt'


def find_answer(diagram: Iterable[str], availability_threshold: int, can_remove=False):
    grid = [l.strip() for l in diagram]
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    answer = 0
    
    def is_occupied(i, j):
        if i < 0 or j < 0 or i == n_rows or j == n_cols or grid[i][j] == '.':
            return False
        else:
            return True
        
    directions = (
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    )
    
    roll_removed = True

    while roll_removed:
        roll_removed = False

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == '@':
                    accessible = sum(is_occupied(i+x, j+y)
                                     for x, y in directions) < availability_threshold

                    if accessible and can_remove:
                        grid[i] = grid[i][:j] + '.' + grid[i][j + 1:]
                        roll_removed = True

                    answer += accessible

    print(f'Answer is {answer}')


EXAMPLE = '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''[1:-1].split('\n')

if True:
    with open(INPUT_FILE) as f:
        find_answer(f, 4, True)
else:
    find_answer(EXAMPLE, 4, True)
