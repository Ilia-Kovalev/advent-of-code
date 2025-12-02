INPUT_FILE = '2025/2_input.txt'


def find_answer(line: str):
    answer = 0
    
    ranges = line.split(',')
    
    for r in ranges:
        b, e = r.split('-')
        b = int(b)
        e = int(e)
        
        invalid_ids = []
        for id in range(b, e + 1):
            id_str = str(id)
            n_digits = len(id_str)

            if n_digits % 2 != 0:
                continue
            
            i_middle = int(n_digits / 2)
            
            if id_str[:i_middle] == id_str[i_middle:]:
                invalid_ids.append(id)

        if invalid_ids:
            message = f'{r} has {len(invalid_ids)} invalid ID(s): '
            message += ', '.join(str(id) for id in invalid_ids) + '.'
            print(message)

            answer += sum(invalid_ids)
        
    print(f'Adding up all the invalid IDs in this example produces {answer}.')
    
with open(INPUT_FILE) as f:
    find_answer(f.readline())
