x = {
    "name": "Ali",
    "age": 25,
    "city": "Tashkent"
}

y = input("Kalit nomini kiriting: ")

z = x.pop(y, None)

if z in x:
    x.pop(y)
    print(f"{y} kaliti o'chirildi.")
else:
    print(f"Bunday kaliy yo'q.")

print("Yangi dict:", x)
