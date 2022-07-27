n = int(input())

values_list, results = [], []

stack = {
    'global': {
        'variable': [],
        'parent': None
    }
}


def add(namesp: str, var: int):

    """
    Adds elements into known namespaces and all variabls into values_list
    :param namesp:
    :param var:
    :return:
    """

    global stack
    stack[namesp]['variable'].append(var)
    values_list.append(var)


def create(namesp: str, parent: str):

    """
    Creates new namespace
    :param namesp:
    :param parent:
    :return:
    """

    global stack
    if namesp not in stack:
        stack[namesp] = {
            'variable': [],
            'parent': parent
        }


def get_var(namesp: str, var: int):

    """
    Returns the namespace of incomming var or None if namespace\var doesn't exsist
    :param namesp:
    :param var:
    :return:
    """

    global stack
    if var not in values_list or namesp not in stack:
        return None
    else:
        return namesp if var in stack[namesp]['variable'] \
            else get_var(stack[namesp]['parent'], var)


for i in range(n):
    command, namesp, var_par = input().split()
    if command == 'add':
        add(namesp, var_par)
    elif command == 'create':
        create(namesp, var_par)
    else:
        res = get_var(namesp, var_par)
        results.append(res)

print(*results, sep='\n')
