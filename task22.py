def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    group = {}
    for i in students:
        group.setdefault(i['group'], []).append(i['name'])

    return group

students = [
    {
        'name': 'Ali',
        'group': 'A'
    },
    {
        'name': 'Vali',
        'group': 'B'
    },
    {
        'name': 'Gani',
        'group': 'A'
    },
    {
        'name': 'Hasan',
        'group': 'A'
    },
]

group = group_students(students)
print(group)
