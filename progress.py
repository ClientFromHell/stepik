# n = int(input())

stack = {
    'global': {
        'variable': [],
        'parent': None
    }
}
vars = []
results = []
TEST_COMMANDS = ['add global a',
                 'create foo global',
                 'add foo b',
                 'get foo a',
                 'get foo c',
                 'create bar foo',
                 'add bar a',
                 'get bar a',
                 'get bar b'
                 ]

stack = {
    'global': {
        'variable': [],
        'parent': None
    }
}

def add(namesp: str, var: int):
    global stack
    stack[namesp]['variable'].append(var)
    vars.append(var)


def create(namesp: str, parent: str):
    global stack
    if namesp not in stack:
        stack[namesp] = {
            'variable': [],
            'parent': parent
        }


def get_var(namesp: str, var: int):
    global stack
    if var not in vars:
        return None
    else:
        return namesp if var in stack[namesp]['variable'] \
            else get_var(stack[namesp]['parent'], var)


for i in TEST_COMMANDS:
    command, namesp, var_par = i.split() # input().split()
    if command == 'add':
        add(namesp, var_par)
    elif command == 'create':
        create(namesp, var_par)
    else:
        res = get_var(namesp, var_par)
        results.append(res)


print(*results, sep='\n')
