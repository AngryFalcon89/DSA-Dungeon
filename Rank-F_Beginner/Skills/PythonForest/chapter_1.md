# 🐍 Awakening Quest: Python Basics - F Rank Dungeon

Welcome, young hunter! You've entered the **Python Forest**, where your first trials await. This scroll contains the sacred runes of **Python**, the chosen language of magic.

---

## 🧠 Programming: The Language of Machines

> "To control the arcane, one must speak its tongue."

* Programming = instructing machines using code.
* Machines understand only 0s and 1s — you must translate!
* Use High-Level Languages like **Python**, **Java**, **C++**.
* Translation done by:

  * 🧙 Interpreter
  * ⚙️ Compiler

---

## 🐍 What is Python?

> "Your first spellbook: Python."

### ⭐ Features of Python

* Simple syntax, readable like English
* Free and open-source
* High-level and portable
* Powers: 🧠 AI, 📊 Data Science, 🌐 Web Dev, 🏗️ Software Dev

---

## 🔥 First Spell Cast (Your First Program)

```python
print("Welcome to the Awakening Quest!")
```

Change the message, cast a new spell:

```python
print(f"Your guide for this quest is {name}, a Rank {rank} hunter.")
print(f"You will start your journey in the {location}.")
```

---

## 📦 Inventory Items: Variables

Variables = containers to store magical values

```python
name = "Hunter Bilal"
rank = "F"
location = "Forest of Beginnings"
energyLevel = 100
questsCompleted = None
readyForQuest = True
```

* `=` is the Assignment Rune
* Variables can change during your journey

### ⚠️ Identifier Rules

1. Start with letters or `_`, not numbers
2. No special characters (!, @, #...)
3. Case-sensitive (`Age` ≠ `age`)
4. Must be meaningful (not `x`, `y`)

---

## 🔢 Data Types

* **int** → whole numbers (`25`, `-5`)
* **float** → decimal values (`3.14`)
* **str** → strings/text (`"Bilal"`)
* **bool** → `True`, `False`
* **None** → empty slot (no magic yet)

```python
print(type(name))   # <class 'str'>
print(type(energyLevel))    # <class 'int'>
```

---

## 🧾 Keywords: Forbidden Runes

Reserved by the language — you can’t use them as variable names:

* `True`, `False`, `None`, `if`, `else`, `for`, `while`, etc.

---

## 🧙 Comments: Notes from Ancient Scribes

```python
# This is a single-line comment
"""
This is a
multi-line comment.
"""
```

---

## ⚔️ Operators: Weapons of Code

### 🧮 Arithmetic Operators

| Operator | Description        | Example (`a=5, b=2`) |
| -------- | ------------------ | -------------------- |
| `+`      | Addition           | `7`                  |
| `-`      | Subtraction        | `3`                  |
| `*`      | Multiplication     | `10`                 |
| `/`      | Division (float)   | `2.5`                |
| `%`      | Modulo (remainder) | `1`                  |
| `**`     | Exponentiation     | `25`                 |
| `//`     | Floor Division     | `2`                  |

### ⚖️ Relational/Comparison Operators

| Operator | Description              |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

### 📝 Assignment Operators

| Operator | Example   | Equivalent to |
| -------- | --------- | ------------- |
| `=`      | `a = 5`   | Assign 5 to a |
| `+=`     | `a += 2`  | `a = a + 2`   |
| `-=`     | `a -= 2`  | `a = a - 2`   |
| `*=`     | `a *= 2`  | `a = a * 2`   |
| `/=`     | `a /= 2`  | `a = a / 2`   |
| `%=`     | `a %= 2`  | `a = a % 2`   |
| `**=`    | `a **= 2` | `a = a ** 2`  |

### 🔗 Logical Operators

| Operator | Description                                   |
| -------- | --------------------------------------------- |
| `and`    | True if both conditions are True              |
| `or`     | True if at least one condition is True        |
| `not`    | Reverses the boolean value (not True → False) |

---

## 🔄 Type Conversion

### 🌀 Implicit (Type Conversion)

* Python auto-converts types

### ✍️ Explicit (Type Casting)

```python
int(), float(), str()
```

```python
a = "2"
b = 4.25
sum = int(a) + b
print(sum) # 6.25
```

---

## 📥 Input from the Dungeon
input() value will always be in `String`, to type cast it we have to use `Explicit Type Casting`.

```python
name = input("Enter your hunter name: ")
age = int(input("Enter your age: "))
```

---

## 🧩 Practice Scrolls (Quests)

### 🎯 Quest 1: Sum of Two Numbers

```python
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
print("Sum =", first + second)
```

### 🎯 Quest 2: Area of a Square

```python
side = float(input("Enter square side: "))
print("Area =", side * side)
```

### 🎯 Quest 3: Average of Two Floats

```python
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Average =", (a + b) / 2)
```

### 🎯 Quest 4: Compare Two Integers

```python
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a >= b)
```

---

> "You’ve completed your first Python Awakening Scroll. Save your progress and prepare to descend deeper into the Dungeons of DSA."