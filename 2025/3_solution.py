from typing import Iterable

INPUT_FILE = '2025/3_input.txt'


def find_answer(banks: Iterable[str]):
    answer = 0
    
    for bank in banks:
        bank = bank.strip()
        first_digit = max(bank[:-1])
        second_digit = max(bank[bank.index(first_digit) + 1:])  
        max_joltage = 10 * int(first_digit) + int(second_digit)
        answer += max_joltage

        print(f'In {bank} max joltage is {max_joltage}')
        
    print(f'Total joltage is {answer}')

with open(INPUT_FILE) as f:
    find_answer(f)
