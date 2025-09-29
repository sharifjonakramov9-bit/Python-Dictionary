def phonebook_menu(phonebook: dict[str, str]) -> None:
    while True:
        print("\n--- Telefon kitobchasi ---")
        print("1. Kontakt qo'shish")
        print("2. Barcha kontaktlarni chiqarish")
        print("3. Ism bo'yicha qidirish")
        print("4. Chiqish")

        choice = input("Tanlang (1-4): ")

        if choice == "1":
            name = input("Ism: ")
            phone = input("Telefon: ")
            phonebook[name] = phone
            print(f"{name} kontakt qo'shildi.")

        elif choice == "2":
            if not phonebook:
                print("Kontaktlar yo'q.")
            else:
                print("Barcha kontaktlar:")
                for name, phone in phonebook.items():
                    print(f"{name}: {phone}")

        elif choice == "3":
            name = input("Qidirilayotgan ism: ")
            if name in phonebook:
                print(f"{name}: {phonebook[name]}")
            else:
                print("Bunday ism yo'q.")

        elif choice == "4":
            print("Dasturni tugatyapmiz...")
            break

        else:
            print("Noto'g'ri tanlov. Qaytadan urinib ko'ring.")

phonebook = {}
print(phonebook_menu(phonebook))
