from typing import Iterable

INPUT_FILE = '2025/12_input.txt'


def find_answer(lines: Iterable[str]):
    shapes = {}
    
    answer = 0
    
    i_current_shape = None
    for l in lines:
        if 'x' not in l:
            if ':' in l:
                i_current_shape = int(l.split(':')[0])
                shapes[i_current_shape] = 0
            else:
                shapes[i_current_shape] += l.count('#')
        else:
            region_size, n_presents = l.strip().split(':')
            field_size = [int(s) for s in region_size.split('x')]
            n_presents = [int(n) for n in n_presents.split()]
            field_square = field_size[0] * field_size[1]
            presents_square = sum(n*shapes[i] for i, n in enumerate(n_presents))
            answer += presents_square <= field_square
            
    print(f'Answer is {answer}')
            


EXAMPLE = iter('''
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
'''[1:-1].split('\n'))


if True:
    with open(INPUT_FILE) as f:
        find_answer(f)
else:
    find_answer(EXAMPLE)
