# 🏛️ Chapter 8: The Temple of Sacred Code - OOP (Object-Oriented Programming)

Welcome, Dungeon Seeker! You've crossed the rivers of functions and climbed the cliffs of file I/O. Now, you step into the **Temple of Sacred Code** where ancient warriors practiced the mystical art of **Object-Oriented Programming** $OOP$. Here, you'll master the power of **Classes, Objects, and Magic Methods** to craft elegant, reusable, and real-world code spells.

---

## 🔮 Why Learn the Sacred Art of OOP?

OOP is not just code; it’s a philosophy, an approach that brings order to chaos:

1. **Procedural Scrolls**: Step-by-step spells, linear and simple.
2. **Functional Tomes**: Modular spell fragments, reusable and sharp.
3. **OOP Grimoire**: The final form. Model anything you imagine — from dragons to datasets.

---

## 🪜 Summoning Classes & Objects

### ✨ Class: The Blueprint Scroll

The **class** defines the spells an object will carry. Like blueprints for summoning potions or swords.

```python
class Adventurer:
    name = "Karan"
```

### 🏹 Object: The Summoned Entity

You summon an instance using the class spell:

```python
s1 = Adventurer()
print(s1.name)  # Output: Karan
```

> Everything in Python is an object! Even swords like `str` or `list`.

---

## 🛡️ The Constructor Spell: `__init__()`

A sacred ritual to give your summoned being its attributes:

```python
class Adventurer:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        print("A new hero enters the realm...")

s1 = Adventurer("Karan", 7)
print(s1.name, s1.level)
```

> `self` refers to the current summoning — the soul of the object.

---

## 🏰 Attributes & Abilities

### ✨ Class Attribute

Shared among all adventurers:

```python
class Adventurer:
    realm = "Dungeonia"
```

### 🧙 Instance Attribute

Unique to each warrior:

```python
    def __init__(self, name):
        self.name = name
```

### ⚔️ Methods: The Warrior's Skills

```python
class Adventurer:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def greet(self):
        print(f"Hail, {self.name}, Level {self.level} Adventurer!")

s1 = Adventurer("Karan", 7)
s1.greet()
```

---

## 🌯 Static Spells: `@staticmethod`

These do not require mana $object$ to cast:

```python
class Temple:
    @staticmethod
    def chant():
        print("The Code is Eternal")

Temple.chant()
```

---

## 🌟 The Pillars of Sacred Coding

### 1. 🏛 Abstraction

Hide the ritual details, show only the outcome:

```python
class Portal:
    def __init__(self):
        self.opened = False

    def activate(self):
        self.opened = True
        print("Portal opens with a shimmer of light...")
```

### 2. 🛡️ Encapsulation

Bundle spell properties and methods together in a sacred class:

```python
class SpellBook:
    def __init__(self, name):
        self.name = name
```

> We've already built encapsulated classes like `Adventurer` and `Portal`

---

## 🎩 Challenge Quest: The Bank of the Undying Vault

Build an `Account` class to manage your gold $balance$, enchanted vault number $acc\_no$, and transactions:

```python
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
```

---

## 🏆 Level Up

You've touched the sacred stones of **OOP**. You're now capable of building real-world entities in your code, just like mighty wizards mold reality. Next awaits the fortress of **Inheritance and Polymorphism** where even greater magic lies.

**Ready your staff, Dungeon Seeker. The path grows deeper and more powerful!**
