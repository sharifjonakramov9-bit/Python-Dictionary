def count_names(names: list[str]) -> dict[str, int]:
    unique_names = set()
    for name in names:
        unique_names.add(name)

    result = {}
    for name in unique_names:
        result[name] = 0

    for name in result.keys():
        result[name] = names.count(name)

    return result

names = ['ali', 'vali', 'gani', 'sami', 'ali', 'gani', 'sami', 'gani']
result = count_names(names)
print(result)
