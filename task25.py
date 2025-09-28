def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    idk = {}
    for i in people:
        idk.setdefault(i["age"], []).append(i["name"])

    return idk

persons = [
    {
        "name": "ali",
        "age": 12
    },
    {
        "name": "vali",
        "age": 14
    },
    {
        "name": "gani",
        "age": 12
    },
    {
        "name": "smai",
        "age": 19
    },
]
people = group_by_age(persons)
print(people)
