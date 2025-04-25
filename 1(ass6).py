class Password_manager:
    def __init__(self):
        self.old_passwords = []

    def get_password(self):
        # Returns the current password, which is the last item in the old_passwords list
        if self.old_passwords:
            return self.old_passwords[-1]
        else:
            return None  # If there is no password set yet

    def set_password(self, new_password):
        # Set the new password only if it's different from all past passwords
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
        else:
            print("Password must be different from the previous passwords.")

    def is_correct(self, password):
        # Check if the provided password is correct (i.e., matches the current password)
        return password == self.get_password()
# Create an instance of the Password_manager
pm = Password_manager()

# Set a new password
pm.set_password("myNewPassword123")

# Check current password
print(pm.get_password())  # Output: myNewPassword123

# Try setting a password that was already used
pm.set_password("myNewPassword123")  # Output: Password must be different from the previous passwords.

# Set a different password
pm.set_password("anotherPassword456")

# Check if a password is correct
print(pm.is_correct("myNewPassword123"))  # Output: False
print(pm.is_correct("anotherPassword456"))  # Output: True

