# permissions.py
ROLE_PERMISSIONS = {
    "admin": ["read_file", "write_file", "delete_file"],
    "user": ["read_file", "write_file"],
    "guest": ["read_file"]
}

def is_authorized(role, action):
    return action in ROLE_PERMISSIONS.get(role, [])
