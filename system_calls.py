# system_calls.py
import time
from permissions import is_authorized

class SecureSystemCallInterface:
    def __init__(self, user, role):
        self.current_user = user
        self.current_role = role
        self.logs = []
        self.log_event(f"Authentication successful for user: {user}")

    def validate_input(self, filename):
        if not isinstance(filename, str) or len(filename) == 0 or '..' in filename or '/' in filename:
            raise ValueError("Invalid filename!")
        return filename

    def read_file(self, filename):
        try:
            filename = self.validate_input(filename)
            if is_authorized(self.current_role, "read_file"):
                self.log_event(f"{self.current_user} read file: {filename}")
                print(f"Reading file: {filename}")
            else:
                self.log_event(f"Unauthorized attempt: {self.current_user} tried to read {filename}")
                print("Permission denied.")
        except Exception as e:
            print(f"Error: {e}")

    def write_file(self, filename, content):
        try:
            filename = self.validate_input(filename)
            if is_authorized(self.current_role, "write_file"):
                self.log_event(f"{self.current_user} wrote to file: {filename}")
                print(f"Writing to file: {filename} -> Content: {content}")
            else:
                self.log_event(f"Unauthorized attempt: {self.current_user} tried to write {filename}")
                print("Permission denied.")
        except Exception as e:
            print(f"Error: {e}")

    def delete_file(self, filename):
        try:
            filename = self.validate_input(filename)
            if is_authorized(self.current_role, "delete_file"):
                self.log_event(f"{self.current_user} deleted file: {filename}")
                print(f"Deleting file: {filename}")
            else:
                self.log_event(f"Unauthorized attempt: {self.current_user} tried to delete {filename}")
                print("Permission denied.")
        except Exception as e:
            print(f"Error: {e}")

    def log_event(self, event):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.logs.append(f"[{timestamp}] {event}")

    def show_logs(self):
        print("\n--- System Call Logs ---")
        for log in self.logs:
            print(log)
