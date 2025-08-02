# 🏰 Chapter 9: Inheritance, Polymorphism & Forbidden Powers

> 🧙 *"You have mastered the temples of classcraft. Now, descend into the Hall of Ancestry, where the runes of **Inheritance**, the veils of **Polymorphism**, and the forbidden glyphs of **Magic Methods** await..."*

---

## 💀 The `del` Curse

The ancient `del` rune banishes attributes or objects into the void. Use with care — once erased, they cannot be summoned again.

```python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shraddha")

# Cast a deletion spell
del s1.name
# print(s1.name)  # ❌ Raises AttributeError

del s1
# print(s1)       # ❌ Raises NameError
```

---

## 🔒 Private Attributes & Shadow Spells

Some scrolls are too powerful to be left unguarded. Prefix attributes or spells with `__` to hide them from outsiders.

```python
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Hidden scroll

    def reset_pass(self):
        print(self.__acc_pass)  # Still accessible within the sanctum

acc1 = Account("12345", "abcde")
print(acc1.acc_no)         # ✅ Allowed
# print(acc1.__acc_pass)   # ❌ Forbidden: AttributeError
acc1.reset_pass()          # ✅ Safe invocation
```

> 🧠 *This technique is called **name mangling** — not absolute protection, but a strong suggestion.*

---

## 🧬 Inheritance: The Bloodline of Code

Just as heroes inherit the powers of their ancestors, **classes** may inherit from others, gaining strength and abilities.

### 🐣 Single Inheritance

```python
class Car:
    @staticmethod
    def start():
        print("Car started...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car1.start()  # 🔥 Inherited power
```

### 🧙 Multi-level Inheritance: The Lineage Tree

```python
class A:
    varA = "Runes of A"
class B(A):
    varB = "Sigils of B"
class C(B):
    varC = "Glyphs of C"

c1 = C()
print(c1.varA)  # A’s rune
print(c1.varB)  # B’s sigil
print(c1.varC)  # C’s glyph
```

### 🕸️ Multiple Inheritance: The Web of Powers

```python
class A:
    varA = "Runes of A"
class B:
    varB = "Sigils of B"
class C(A, B):
    varC = "Glyphs of C"

c1 = C()
print(c1.varA)
print(c1.varB)
```

### 🪜 `super()`: Summon the Ancestor

```python
class Car:
    def __init__(self, type):
        self.type = type

class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  # Summoning ancient constructor
        self.name = name

car1 = ToyotaCar("Prius", "Electric")
print(car1.type)
```

---

## 🕯️ Class Methods: Alters of the Bloodline

Summon spells that act on the **class itself**, not just one adventurer.

```python
class Person:
    name = "anonymous"  # Class glyph

    @classmethod
    def change_name(cls, name):
        cls.name = name  # Alters the scroll for all

p1 = Person()
p1.change_name("Rahul Kumar")
print(p1.name)      # Rahul Kumar
print(Person.name)  # Also Rahul Kumar
```

| Spell Type     | First Rune | Affects | Decorator       |
| -------------- | ---------- | ------- | --------------- |
| Instance Spell | `self`     | Object  | *(none)*        |
| Class Spell    | `cls`      | Class   | `@classmethod`  |
| Static Spell   | *(none)*   | Neither | `@staticmethod` |

---

## 🧾 Property Scrolls (`@property`)

Some values must be summoned indirectly through ritual — that's where `@property` scrolls shine.

```python
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)  # Auto-updates!
```

---

## 🧙‍♂️ Polymorphism: The Many-Faced Glyph

> *“One glyph, many forms” — an incantation that behaves differently depending on context.*

### Examples in the Wild:

* `1 + 2` ➜ Math addition
* `"Hi" + "There"` ➜ String merge
* `[1, 2] + [3, 4]` ➜ List fusion

---

## ✨ Operator Overloading with Dunder Spells

To override basic glyphs like `+`, `>`, or `==`, we cast **dunder methods** like `__add__`, `__gt__`, etc.

```python
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):  # Override the ">" rune
        return self.price > other.price

order1 = Order("Chips", 20)
order2 = Order("Tea", 15)

print(order1 > order2)  # 🔥 True, the glyph was overloaded
```

---

## 🏁 Dungeon Complete!

> 🧡 *You now hold the ancient secrets of code inheritance and polymorphic spellcraft. Few reach this tier. In the next chamber, even deeper magic awaits — the realm of modules, packages, and code organization.*

---
🎮 **Rank Progress: F → F+**

🏷️ *Commit your scrolls to the Dungeon Codex (GitHub), and return for your next quest.*