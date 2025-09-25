permissions = {"read": True, "write": False, "delete": True}
# chiqishi: read, delete

for key in permissions:
    if permissions[key]:
        print(key)

