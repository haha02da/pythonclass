users = {"Hans": "active", "Éléonore": "inactive", "Ken": "active"}

for user, status in users.copy().items():
    if status == "inactive":
        del users[user]
print(users)

inactive_users = {}
for user, status in users.items():
    if status == "inactive":
        inactive_users[user] = status

print(inactive_users)

print(list(range(10,0,-1)))