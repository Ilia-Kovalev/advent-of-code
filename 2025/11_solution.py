from typing import Iterable, List
import networkit as nk

INPUT_FILE = '2025/11_input.txt'


def find_answer(lines: Iterable[str], src: str, dest: str, required: List[str] = None):
    g = nk.Graph(directed=True)
    
    node_mapper = {}
    
    for l in lines:
        node, outputs = l.strip().split(':')
        outputs = outputs.split()
        
        for n in [node] + outputs:
            if n not in node_mapper:
                node_mapper[n] = g.addNode()
        
        for o in outputs:
            g.addEdge(node_mapper[node], node_mapper[o])
    
    if required:
        answer = 1
        cur_src = src
        for req in required + [dest]:
            answer *= nk.reachability.AllSimplePaths(
                g, node_mapper[cur_src], node_mapper[req]).run().numberOfSimplePaths()
            cur_src = req
    else:
        answer = nk.reachability.AllSimplePaths(
            g, node_mapper[src], node_mapper[dest]).run().numberOfSimplePaths()


    print(f"Answer is {answer}")


EXAMPLE1 = iter('''
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
'''[1:-1].split('\n'))

EXAMPLE2 = iter('''
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
'''[1:-1].split('\n'))


if True:
    with open(INPUT_FILE) as f:
        find_answer(f, 'svr', 'out', ['fft', 'dac'])
else:
    find_answer(EXAMPLE2, 'svr', 'out', ['fft', 'dac'])
