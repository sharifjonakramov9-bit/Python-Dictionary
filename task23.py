def group_indices(numbers: list[int]) -> dict[int, list[int]]:
    result = {}
    for i, n in enumerate(numbers):
        result.setdefault(n, []).append(i)

    return result

numbers = [1, 1, 1, 2, 3, 4, 5, 5, 6, 6]

print(group_indices(numbers))
