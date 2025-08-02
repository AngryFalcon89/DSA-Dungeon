# 🕵️‍♂️ Chapter 5: The Looping Labyrinth

>🎧 *"Through the spiral halls of time you now walk, where repetition carves runes of logic and rhythm powers the arcane. Welcome, adventurer, to the **Looping Labyrinth** where while-beasts and for-spirits dwell!"*

---

## 🪩 The Concept of Loops

A **loop** is a temporal spell that **repeats** a block of code until a condition breaks its enchantment. Think of it as casting a chant again and again until your mana depletes or the world changes.

In Python, there are two types of loops:

1. 🌍 **`while` Loops** - conditional chants
2. ✨ **`for` Loops** - elemental traversals

---

## ⏳ `while` Loop: The Temporal Chant

```python
count = 1
while count <= 5:
    print("🔮 Hello, adventurer!")
    count += 1
```

* Starts with a condition (like a magical trigger).
* Executes the code block until the condition fades (False).

🚨 **Beware! Infinite Chanting**

```python
# while True:
#     print("♻️ Shield Activated...")
```

This will trap you in an **infinite loop of doom** if left unchecked.

---

## ⚔️ Practice Scrolls: `while` Loop

### ✅ Quest 1: Print 1 to 100

```python
i = 1
while i <= 100:
    print(i)
    i += 1
```

### ❌ Quest 2: Print 100 to 1

```python
i = 100
while i >= 1:
    print(i)
    i -= 1
```

### 🌊 Quest 3: Multiplication Spell

```python
n = int(input("Enter number: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1
```

### 🛠️ Quest 4: Traverse the Sigil List

```python
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1
```

---

## 🔀 Loop Control Runes

### ❌ `break` - Escape Portal

Ends the loop spell immediately.

```python
nums = (1, 4, 9, 16, 36, 49)
x = 36
i = 0
while i < len(nums):
    if nums[i] == x:
        print("✨ Found at", i)
        break
    i += 1
```

### ⏭️ `continue` - Skip Chant

Skips current iteration, continues next.

```python
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
```

---

## 🧙‍♂️ `for` Loop: Spirit Walker

Traverses items in a magical sequence:

```python
veggies = ["potato", "brinjal", "ladyfinger"]
for veg in veggies:
    print(veg)
```

```python
word = "Dungeon"
for ch in word:
    print(ch)
```

---

### 📆 `else` in Loops

Executed if loop ends **normally** (not by `break`).

```python
for ch in "Dungeon":
    if ch == 'o':
        break
else:
    print("✅ End of sequence")
```

---

## ⏱ `range()` Function: Time Gate Generator

```python
for i in range(5):
    print(i)  # 0 to 4

for i in range(2, 5):
    print(i)  # 2 to 4

for i in range(2, 10, 2):
    print(i)  # even numbers: 2, 4, 6, 8
```

---

### 🔢 Practice Scrolls: `for` + `range()`

#### 1. Numbers 1 to 100

```python
for i in range(1, 101):
    print(i)
```

#### 2. Numbers 100 to 1

```python
for i in range(100, 0, -1):
    print(i)
```

#### 3. Multiplication Spell

```python
n = int(input("Enter number: "))
for i in range(1, 11):
    print(n * i)
```

---

## 🏛 `pass` Spell: Null Incantation

```python
for i in range(5):
    pass  # Placeholder rune

print("Work continues...")
```

---

## 🪄 Final Challenges

### 🔢 Sum of first `n` natural numbers (while)

```python
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Total sum =", sum)
```

### 🪩 Factorial of `n` (for)

```python
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)
```

---

## 🌟 Chapter Complete

> 🦜 "You have now mastered the labyrinth of loops and control runes. Ahead lies the Twilight Gate of Functions—where custom spells and scroll-binding rituals await."

---
