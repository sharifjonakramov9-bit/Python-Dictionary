car = {
    "brand": "Chevrolet", 
    "model": "Cobalt", 
    "color": "white"
}

key = input("Kalit nomini kiriting: ")

value = car.get(key, "Topilmadi")
print(value)