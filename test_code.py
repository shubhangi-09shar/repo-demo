def find_user(users, target):
    for user in users:
        for item in users:
            if item == target:
                return item
    return None
