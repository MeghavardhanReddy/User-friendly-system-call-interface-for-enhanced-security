# user_auth.py
USER_DATABASE = {
    "admin": "admin123",
    "user1": "password1",
    "guest": "guestpass"
}

USER_ROLES = {
    "admin": "admin",
    "user1": "user",
    "guest": "guest"
}

def authenticate(username, password):
    if username in USER_DATABASE and USER_DATABASE[username] == password:
        return True, USER_ROLES.get(username, "guest")
    return False, None
