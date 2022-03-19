
user_database = {
    'user': 'password',
    'iseedeadpeople': 'greedisgood',
    'hesoyam': 'tgm'
}

def check_user(username, password):
    if username in user_database.keys():
        if user_database[username] == password:
            return True
    return False

print(check_user('hesoyam', 'tgm'))