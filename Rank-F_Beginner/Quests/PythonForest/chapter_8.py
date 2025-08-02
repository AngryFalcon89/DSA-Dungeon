# 🏛️ Chapter 8: The Temple of Sacred Code - OOP (Object-Oriented Programming)

# Summoning Classes & Objects

# ✨ Class: The Blueprint Scroll
class Adventurer:
    name = "Karan"

# 🏹 Object: The Summoned Entity
s1 = Adventurer()
print(s1.name)  # Output: Karan


# 🛡️ The Constructor Spell: __init__()
class Adventurer:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        print("A new hero enters the realm...")

s1 = Adventurer("Karan", 7)
print(s1.name, s1.level)


# 🏰 Attributes & Abilities

# ✨ Class Attribute
class Adventurer:
    realm = "Dungeonia"

# 🧙 Instance Attribute
class Adventurer:
    def __init__(self, name):
        self.name = name

# ⚔️ Methods: The Warrior's Skills
class Adventurer:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def greet(self):
        print(f"Hail, {self.name}, Level {self.level} Adventurer!")

s1 = Adventurer("Karan", 7)
s1.greet()


# 🌯 Static Spells: @staticmethod
class Temple:
    @staticmethod
    def chant():
        print("The Code is Eternal")

Temple.chant()


# 🌟 The Pillars of Sacred Coding

# 1. 🏛 Abstraction
class Portal:
    def __init__(self):
        self.opened = False

    def activate(self):
        self.opened = True
        print("Portal opens with a shimmer of light...")


# 2. 🛡️ Encapsulation
class SpellBook:
    def __init__(self, name):
        self.name = name


# 🎩 Challenge Quest: The Bank of the Undying Vault
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

    def debit(self, amount):
        self.balance -= amount
        print(f"-{amount} gold debited. Remaining balance: {self.get_balance()}")

    def credit(self, amount):
        self.balance += amount
        print(f"+{amount} gold credited. New balance: {self.get_balance()}")

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)
