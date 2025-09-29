def most_common_char(text: str) -> str:
    mx = text[0]
    for ch in text:
        if text.count(ch) > text.count(mx):
            mx = ch

    return mx

text = 'dsaogyfaygdoaorygoaugyrouafvaudsygofagoygeoyrobdaoybgygaoyvenytystrnuctvoiuyriorytvsoinygtvrosirngvoisrngtv'

idk = most_common_char(text)

print(idk)
