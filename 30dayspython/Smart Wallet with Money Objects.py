class Money:
    def __init__(self, amount: float, currency: str = "Rs"):
        self.amount = amount
        self.currency = currency

    def __str__(self) -> str:
        # Returns user-friendly format using an f-string
        return f"{self.currency} {self.amount}"

    def __repr__(self) -> str:
        # Returns developer-focused debugging format
        return f"Money({self.amount}, '{self.currency}')"

    def __add__(self, other: "Money") -> "Money":
        # Returns a completely new Money instance without mutating originals
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount == other.amount and self.currency == other.currency

    def __lt__(self, other: "Money") -> bool:
        # Providing __lt__ is sufficient for Python's sorted() to work
        if not isinstance(other, Money):
            return NotImplemented
        return self.amount < other.amount


class Wallet:
    def __init__(self, money_list: list[Money] = None):
        self.items = money_list if money_list is not None else []

    def __len__(self) -> int:
        # Returns total count of notes inside the wallet
        return len(self.items)

    def total(self) -> Money:
        # Avoids plain sum() int initialization issues by looping manually
        if not self.items:
            return Money(0)
        
        total_amount = 0
        currency = self.items[0].currency
        
        for item in self.items:
            total_amount += item.amount
            
        return Money(total_amount, currency)


# --- Verification Code Matching Your Sample Run ---
if __name__ == "__main__":
    a = Money(500)
    b = Money(300)
    
    print(a + b)            # Output: Rs 800
    print(a == Money(500))  # Output: True (Note: fixed sample run typo 'a = Money')
    print(b < a)            # Output: True
    
    notes = [Money(100), Money(500), Money(50)]
    print(sorted(notes))    # Output: [Money(50, 'Rs'), Money(100, 'Rs'), Money(500, 'Rs')]
    
    w = Wallet(notes)
    print(len(w))           # Output: 3
    print(w.total())        # Output: Rs 650
