import re

INPUT_FILE = '2025/2_input.txt'


def find_answer(line: str, i_part: int):
    answer = 0
    
    ranges = line.split(',')
    
    match i_part:
        case 1:
            matcher = re.compile(r'((^\d+)\2$)')
        case 2:
            matcher = re.compile(r'((^\d+)\2+$)')
        case _:
            raise ValueError(f'Unexpected part {i_part}')

    for r in ranges:
        b, e = r.split('-')
        b = int(b)
        e = int(e)
        
        invalid_ids = []
        for id in range(b, e + 1):
            if matcher.match(str(id)):
                invalid_ids.append(id)

        if invalid_ids:
            message = f'{r} has {len(invalid_ids)} invalid ID(s): '
            message += ', '.join(str(id) for id in invalid_ids) + '.'
            print(message)

            answer += sum(invalid_ids)
        
    print(f'Adding up all the invalid IDs in this example produces {answer}.')
    
with open(INPUT_FILE) as f:
    find_answer(f.readline(), 2)
