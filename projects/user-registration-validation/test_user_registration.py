from registration import register_user

users_dict = {
    'user1':
        {
            "name": 'Baby',
            "email": "baby@gmail.com",
            "password":'Baby124@'
        },
        'user1':
        {
            "name": '',
            "email": "baby@gmail.com",
            "password":'Baby124@'
        }
}

for users in users_dict:
    users = register_user(users_dict[users]["name"], users_dict[users]["email"], users_dict[users]["password"])
    print(users)