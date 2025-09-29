def filter_non_zero(d: dict[str, int]) -> dict[str, int]:
    result = {}

    for key, value in d.items():
        if value != 0:
            result[key] = value

    return result

d = {
    "a": 0,
    "b": 5, 
    "c": 0, 
    "d": 7
}

print(filter_non_zero(d))
