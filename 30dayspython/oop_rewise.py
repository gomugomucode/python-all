# Encapsulation & Name Mangling

class SecureVault:
    def __init__(self, owner: str, initial_key: str):
        self.owner = owner
        self.__vault_key = initial_key  # Strictly private attribute
        self.__access_logs = []         # Internal tracking array

    def view_logs_mangled(self):
        # Name mangling applies internally to the class automatically
        return self.__access_logs

# Test
vault = SecureVault("Director", "Alpha-99X")
print(f"Vault Owner: {vault.owner}")
# print(vault.__vault_key) # Throws AttributeError

# Accessing both private variables externally via explicit name mangling
print(f"Mangled Key: {vault._SecureVault__vault_key}")
print(f"Mangled Logs: {vault._SecureVault__access_logs}")

# Getters, Setters & Property Validationpython
class PremiumSubscription:
    def __init__(self, user_email: str, monthly_slots: int):
        self.user_email = user_email
        self._slots = monthly_slots

    @property
    def slots(self) -> int:
        """Getter returns current available slots."""
        return self._slots

    @slots.setter
    def slots(self, new_count: int):
        """Setter enforces type checking and strict boundary limits."""
        if not isinstance(new_count, int):
            raise TypeError("Slot count must be a whole number.")
        if not (1 <= new_count <= 100):
            raise ValueError("Slots must scale between 1 and 100 profiles.")
        self._slots = new_count

# Test
sub = PremiumSubscription("user@stream.io", 5)
sub.slots = 12       # Updates smoothly
print(f"Updated slots: {sub.slots}")
# sub.slots = 150    # Triggers ValueError
# sub.slots = "five" # Triggers TypeError