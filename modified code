import os
import time

# Dummy user database
USER_DATABASE = {
    "admin": "admin123",
    "user1": "password1",
    "guest": "guestpass"
}

# Roles and permissions
ROLE_PERMISSIONS = {
    "admin": ["read_file", "write_file", "delete_file"],
    "user": ["read_file", "write_file"],
    "guest": ["read_file"]
}

# Map username to roles
USER_ROLES = {
    "admin": "admin",
    "user1": "user",
    "guest": "guest"
}

# Secure System Call Interface
class SecureSystemCallInterface:
    def __init__(self):
        self.current_user = None
        self.current_role = None
        self.logs = []

    # Authentication
    def authenticate(self, username, password):
        if username in USER_DATABASE and USER_DATABASE[username] == password:
            self.current_user = username
            self.current_role = USER_ROLES.get(username, "guest")
            self.log_event(f"Authentication successful for user: {username}")
            print(f"Welcome {username}! Role: {self.current_role}")
            return True
        else:
            self.log_event(f"Authentication failed for user: {username}")
            print("Authentication failed!")
            return False

    # Input validation
    def validate_input(self, filename):
        if not isinstance(filename, str) or len(filename) == 0 or '..' in filename or '/' in filename:
            raise ValueError("Invalid filename!")
        return filename

    # Authorization
    def is_authorized(self, action):
        allowed = action in ROLE_PERMISSIONS.get(self.current_role, [])
        if not allowed:
            self.log_event(f"Unauthorized attempt: {self.current_user} tried to {action}")
        return allowed

    # Real File Operations
    def read_file(self, filename):
        try:
            filename = self.validate_input(filename)
            if self.is_authorized("read_file"):
                if os.path.exists(filename):
                    with open(filename, 'r') as f:
                        content = f.read()
                    self.log_event(f"{self.current_user} read file: {filename}")
                    print(f"\n--- File Content ---\n{content}\n---------------------")
                else:
                    print("File does not exist.")
        except Exception as e:
            print(f"Error: {e}")

    def write_file(self, filename, content):
        try:
            filename = self.validate_input(filename)
            if self.is_authorized("write_file"):
                with open(filename, 'w') as f:
                    f.write(content)
                self.log_event(f"{self.current_user} wrote to file: {filename}")
                print(f"File '{filename}' written successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def delete_file(self, filename):
        try:
            filename = self.validate_input(filename)
            if self.is_authorized("delete_file"):
                if os.path.exists(filename):
                    os.remove(filename)
                    self.log_event(f"{self.current_user} deleted file: {filename}")
                    print(f"File '{filename}' deleted successfully.")
                else:
                    print("File does not exist.")
        except Exception as e:
            print(f"Error: {e}")

    # Logging
    def log_event(self, event):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.logs.append(f"[{timestamp}] {event}")

    # Display Logs
    def show_logs(self):
        print("\n--- System Call Logs ---")
        for log in self.logs:
            print(log)

# Driver Code
if __name__ == "__main__":
    interface = SecureSystemCallInterface()
    
    print("=== Secure System Call Interface ===")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if interface.authenticate(username, password):
        while True:
            print("\nAvailable Actions:")
            print("1. Read File")
            print("2. Write File")
            print("3. Delete File")
            print("4. Show Logs")
            print("5. Exit")

            choice = input("Select an action (1-5): ")

            if choice == "1":
                filename = input("Enter filename to read: ")
                interface.read_file(filename)
            elif choice == "2":
                filename = input("Enter filename to write: ")
                content = input("Enter content to write: ")
                interface.write_file(filename, content)
            elif choice == "3":
                filename = input("Enter filename to delete: ")
                interface.delete_file(filename)
            elif choice == "4":
                interface.show_logs()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
    else:
        print("Access Denied.")
