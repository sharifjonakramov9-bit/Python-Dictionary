def count_letters(text: str) -> dict[str, int]:
    idk = {}
    for ch in text:
        if ch != " ":
            idk[ch] = idk.get(ch, 0) + 1

    return idk

print(count_letters("assalomu alaykum"))
