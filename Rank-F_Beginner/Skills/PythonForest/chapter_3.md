# 🏰 Chapter 3: The Vault of Lists & Tuples

> 🔊 "Enter the halls where enchanted scrolls of sequences dwell. Welcome to the Vault of Lists and the Pillars of Tuples!"

---

## 🔢 Quest 1: The Scrolls of Lists

Lists are **enchanted containers** that hold various types of data—from potions to spells, all in one magical sequence.

### 🌈 Forging the List Scroll

```python
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))  # <class 'list'>
print(marks[1])     # 87.5
```

### 🛍️ List Traits

* ✨ **Index Magic**: Use positions to retrieve values.
* ⏳ **Length Spell**: `len(list)` counts your items.
* ⚔️ **Mixed Potions**: Combine string, int, etc.

```python
student = ["Hunter Bilal", 95, "Weakest Hunter of all time"]
print(student)
```

### 🔄 Mutability Charm

```python
student[1] = 97
print(student)  # ["Hunter Bilal", 97, "Weakest Hunter of all time"]
```

### 🔍 Slice and Scry

```python
marks = [85, 94, 76, 63, 48]
print(marks[1:4])  # [94, 76, 63]
print(marks[-3:-1])  # [76, 63]
```

---

## 🔧 Enchantments: List Methods

* `.append(x)` ➔ Attach a new rune
* `.sort()` ➔ Align by value
* `.sort(reverse=True)` ➔ Align by value in descending order
* `.reverse()` ➔ Flip the scroll
* `.insert(idx, el)` ➔ Embed rune at spot
* `.remove(x)` ➔ Destroy first match
* `.pop(idx)` ➔ Vanish rune by index

```python
inventory = ["sword", "potion"]
inventory.append("shield")
inventory.sort()
print(inventory)
```

---

## 🏛️ Quest 2: The Pillars of Tuples

Tuples are **unbreakable scrolls**. Once scribed, their runes cannot be changed.

### ✨ Conjuring a Tuple

```python
tup = (94.4, 87.5, 95.2)
tup2 = (1,) # for creating single values tuple!, else it will be of type <class> int.
print(tup)
```

### ⛓ Immutable Edict

```python
tup[0] = 5  # ❌ Forbidden! Raises TypeError
```

### 🔍 Tuple Scrying

```python
tup = (1, 2, 3, 2)
print(tup.index(2))  # 1
print(tup.count(2))  # 2
```

---

## 🌟 Practice Scrolls

### 🎬 Q1: Favorite Memory Scrolls

```python
skill = []
for i in range(3):
    skill.append(input(f"Enter favorite skill {i+1}: "))
print("Your favorite skill:", skill)
```

### ⚔️ Q2: Palindrome Rune Test

```python
list1 = [1, 2, 3, 2, 1]
if list1 == list1[::-1]:
    print("🌟 Palindrome Scroll!")
else:
    print("❌ Not a Palindrome")
```

### 📙 Q3: Grade Count Incantation

```python
grades = ("C", "D", "A", "A", "B", "B", "A")
print("'A' runes counted:", grades.count("A"))  # 3
```

### 🌟 Q4: Sort the Grade Relics

```python
grades = ["C", "D", "A", "A", "B", "B", "A"]
grades.sort()
print("Sorted grades:", grades)  # ['A', 'A', 'A', 'B', 'B', 'C', 'D']
```

---

## 🏋️ Chapter Complete

> 🧙 "You have conquered the Vault of Lists and deciphered the Pillars of Tuples. Next lies the Looping Labyrinth where time bends to your will..."

---
