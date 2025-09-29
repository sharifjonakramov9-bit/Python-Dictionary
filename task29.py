def get_active_users(users: dict[str, dict[str, bool | str]]) -> list[str]:
    idk = []
    for name, i in users.items():
        if i["active"]:
            idk.append(name)
    return idk

users = {
    "Ali": {"email": "ali@example.com", "active": True},
    "Vali": {"email": "vali@example.com", "active": False},
    "Hasan": {"email": "hasan@example.com", "active": True},
}

print(get_active_users(users))
