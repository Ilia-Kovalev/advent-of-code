from typing import Iterable
import numpy as np
from scipy.optimize import linprog

INPUT_FILE = '2025/10_input.txt'


def find_answer(lines: Iterable[str]):
    answer = 0
    answer2 = 0

    for line in lines:
        parts = line.strip().split(' ')
        joltage = parts.pop()
        buttons = parts[1:]

        expected_state = tuple([True if ch == '#' else False for ch in parts[0][1:-1]])
        joltage = np.array([int(v) for v in joltage[1:-1].split(',')])

        buttons = [[int(i) for i in button[1:-1].split(',')] for button in buttons]
        buttons = [tuple(True if i in b else False for i in range(len(expected_state))) for b in buttons]

        known_states = set([tuple([False] * len(expected_state))])
        states_to_check = set(buttons)
                        
        i_steps = 1
        while not expected_state in states_to_check:
            i_steps += 1

            new_states = set()
            for state in states_to_check:
                for button in buttons:
                    new_states.add(tuple(s != b for s, b in zip(state, button)))
            
            known_states |= states_to_check
            new_states -= known_states
            states_to_check = new_states

        answer += i_steps

        solution = linprog(np.ones((len(buttons),)),
                           A_eq=np.array(buttons, int).T, b_eq=joltage, integrality=1)
        print(solution)
        answer2 += solution.fun

    print(f"Answer is {answer}")
    print(f"Answer2 is {answer2}")



EXAMPLE = iter('''
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
'''[1:-1].split('\n'))


if True:
    with open(INPUT_FILE) as f:
        find_answer(f)
else:
    find_answer(EXAMPLE)
