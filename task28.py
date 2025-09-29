def group_by_length(words: list[str]) -> dict[int, list[str]]:
    result = {}
    for word in words:
        idk = len(word)
        result.setdefault(idk, []).append(word)
    return result


words = ["Ali", "Vali", "Salom", "kitob", "AI"]
print(group_by_length(words))
