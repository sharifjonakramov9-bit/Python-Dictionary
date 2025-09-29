def merge_dicts(a: dict, b: dict) -> dict:

    result = a.copy()
    result.update(b)
    
    x = set()
    y = {}

    for k, v in result.items():
        if v not in x:
            y[k] = v
            x.add(v)

    return y

a = {'a': 1, 'b': 2, 'd': 5}
b = {'x': 3, 'c': 4, 'f': 5}

idk = merge_dicts(a, b)
print(idk)
