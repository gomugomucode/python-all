# # Encapsulation & Name Mangling

# class SecureVault:
#     def __init__(self, owner: str, initial_key: str):
#         self.owner = owner
#         self.__vault_key = initial_key  # Strictly private attribute
#         self.__access_logs = []         # Internal tracking array

#     def view_logs_mangled(self):
#         # Name mangling applies internally to the class automatically
#         return self.__access_logs

# # Test
# vault = SecureVault("Director", "Alpha-99X")
# print(f"Vault Owner: {vault.owner}")
# # print(vault.__vault_key) # Throws AttributeError

# # Accessing both private variables externally via explicit name mangling
# print(f"Mangled Key: {vault._SecureVault__vault_key}")
# print(f"Mangled Logs: {vault._SecureVault__access_logs}")


# # Getters, Setters & Property Validationpython
# class PremiumSubscription:
#     def __init__(self, user_email: str, monthly_slots: int):
#         self.user_email = user_email
#         self._slots = monthly_slots

#     @property
#     def slots(self) -> int:
#         """Getter returns current available slots."""
#         return self._slots

#     @slots.setter
#     def slots(self, new_count: int):
#         """Setter enforces type checking and strict boundary limits."""
#         if not isinstance(new_count, int):
#             raise TypeError("Slot count must be a whole number.")
#         if not (1 <= new_count <= 100):
#             raise ValueError("Slots must scale between 1 and 100 profiles.")
#         self._slots = new_count

# # Test
# sub = PremiumSubscription("user@stream.io", 5)
# sub.slots = 12       # Updates smoothly
# print(f"Updated slots: {sub.slots}")
# # sub.slots = 150    # Triggers ValueError
# # sub.slots = "five" # Triggers TypeError



# # Inheritance and super()python 
# class CloudService:
#     def __init__(self, region: str, monthly_budget: float):
#         self.region = region
#         self.monthly_budget = monthly_budget

# class ComputeInstance(CloudService):
#     def __init__(self, region: str, monthly_budget: float, core_count: int, ram_gb: int):
#         # Forward configuration to parent constructor
#         super().__init__(region, monthly_budget)
#         self.core_count = core_count
#         self.ram_gb = ram_gb

# # Test
# server = ComputeInstance("us-east-1", 120.00, 8, 32)
# print(f"Server deployed in {server.region} with {server.ram_gb}GB RAM.")


# # . Multiple Inheritance and MRO (The Diamond Problem)python 
# class Asset:
#     def get_status(self): return "Base Asset active."

# class IntellectualProperty(Asset):
#     def get_status(self): return "IP protected by copyright."

# class PhysicalProperty(Asset):
#     def get_status(self): return "Physical storage verified."

# class DigitalArtwork(IntellectualProperty, PhysicalProperty):
#     """Inherits from two child classes sharing the same base parent."""
#     pass

# # Test
# nft = DigitalArtwork()
# # Follows MRO: Left-to-right, depth-first, then up to the common ancestor
# print(f"Resolved execution: {nft.get_status()}") 
# print("\n MRO Resolution Chain:")
# for target_class in DigitalArtwork.__mro__:
#     print(f" -> {target_class.__name__}")



# # Polymorphism & Method Overridingpython 
# class DataCompressor:
#     def compress(self, file_path: str) -> str:
#         return f"Standard archiving for {file_path}"

# class ZipCompressor(DataCompressor):
#     def compress(self, file_path: str) -> str:
#         return f"Deflate compression algorithm applied to {file_path}.zip"

# class TarGzCompressor(DataCompressor):
#     def compress(self, file_path: str) -> str:
#         return f"Gzip compression system applied to {file_path}.tar.gz"

# # Test polymorphic execution loop
# workers = [ZipCompressor(), TarGzCompressor(), DataCompressor()]
# for engine in workers:
    # print(engine.compress("logs/today"))



# # Duck Typing & Mixinspython 
# class ExportPDFMixin:
#     def generate_pdf(self):
#         return f"PDF generated for {id(self)}"

# class Invoice(ExportPDFMixin):
#     def display_billing(self): return "Billing Details"

# # Two entirely unrelated classes sharing matching method signatures
# class SpeedBoat:
#     def move(self): return "Slicing through ocean waves."

# class SpaceShuttle:
#     def move(self): return "Breaking orbit entry velocities."

# def launch_sequence(vehicle_obj):
#     """Duck Typing: Expects a move() method. Does not care about class family."""
#     print(f"Launch report: {vehicle_obj.move()}")

# # Test Mixin and Duck Typing
# bill = Invoice()
# print(bill.generate_pdf())  # Mixin added function completely out of context

# boat, ship = SpeedBoat(), SpaceShuttle()
# launch_sequence(boat)       # Works perfectly
# launch_sequence(ship)       # Works perfectly



#  Abstraction (ABC, @abstractmethod)python 
from abc import ABC, abstractmethod

class GameController(ABC):
    @abstractmethod
    def press_action_button(self) -> str:
        pass

class PlayStationController(GameController):
    def press_action_button(self) -> str:
        return "X button registered on DualSense."

class XboxController(GameController):
    def press_action_button(self) -> str:
        return "A button registered on Core Controller."

# Test abstraction implementation rules
# basic_pad = GameController() # Throws TypeError (Cannot instantiate)
ps5 = PlayStationController()
series_x = XboxController()
print(ps5.press_action_button())
print(series_x.press_action_button())



# Magic Methods (__str__ and __repr__)python
class ServerNode:
    def __init__(self, ip_address: str, node_id: int):
        self.ip_address = ip_address
        self.node_id = node_id

    def __str__(self) -> str:
        """Clean string for frontend readouts, terminal dashboards, or logs."""
        return f"Node-{self.node_id} ({self.ip_address})"

    def __repr__(self) -> str:
        """Formal code replication representation intended for debugging runs."""
        return f"ServerNode(ip_address='{self.ip_address}', node_id={self.node_id})"

# Test
node = ServerNode("192.168.1.45", 801)
print(str(node))   # Returns: Node-801 (192.168.1.45)
print(repr(node))  # Returns: ServerNode(ip_address='192.168.1.45', node_id=801)






# Iterators & Generatorspython
class StepValueIterator:
    """Custom iterator stepping forwards by specific configurations."""
    def __init__(self, stop: int, step: int):
        self.stop = stop
        self.step = step
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += self.step
        return val

def step_value_generator(stop: int, step: int):
    """Shorter generator tracking exact matching stepping sequences."""
    curr = 0
    while curr < stop:
        yield curr
        curr += step

# Test both structures
print("Iterator output:", list(StepValueIterator(15, 3)))
print("Generator output:", list(step_value_generator(15, 3)))





#  Decoratorspython
def validation_gate(func):
    """Decorator checking argument types before execution run."""
    def wrapper(*args, **kwargs):
        print("[GATEWAY]: Verifying parameter rules...")
        for argument in args:
            if isinstance(argument, str) and len(argument) < 3:
                return "Operation Cancelled: String entry too short."
        return func(*args, **kwargs)
    return wrapper

@validation_gate
def register_profile(username: str):
    return f"Profile verified and saved for {username}."

# Test cases
print(register_profile("Administrator")) # Runs completely
print(register_profile("ex"))            # Intercepted and blocked by gate


