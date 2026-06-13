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
