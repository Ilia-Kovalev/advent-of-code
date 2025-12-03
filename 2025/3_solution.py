from typing import Iterable

INPUT_FILE = '2025/3_input.txt'


def find_answer(banks: Iterable[str], n_batteries: int):
    answer = 0
    
    for bank in banks:
        bank = bank.strip()
        max_joltage = 0
        i_last = -1

        for i in range(n_batteries):
            current_slice = bank[i_last + 1: len(bank) - (n_batteries - i) + 1]
            battary_joltage = max(current_slice)
            i_last = current_slice.index(battary_joltage) + i_last + 1
            max_joltage += 10 ** (n_batteries - i - 1) * int(battary_joltage)

        answer += max_joltage
        print(f'In {bank} max joltage is {max_joltage}')

    print(f'Total joltage is {answer}')

with open(INPUT_FILE) as f:
    find_answer(f, 12)
