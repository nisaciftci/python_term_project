import hashlib
from file_manager import save_data

def make_secure(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(users, username, password):
    if username in users:
        print("Error: Username taken!")
        return False
    
    users[username] = {
        "password": make_secure(password),
        "balance": 0.0,
        "history": []
    }
    save_data(users)
    print("User created successfully!")
    return True

def login_user(users, username, password):
    if username in users:
        real_password = users[username]["password"]
        input_password = make_secure(password)

        if real_password == input_password:
            return True
        
    print("Login failed!")
    return False
