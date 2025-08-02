# 🏰 Chapter 2: The Strings & Conditional Caverns

> 💬 "The world is made of decisions and words. Welcome to the String Catacombs and the Chambers of Conditions!"

---

## 🧵 Quest 1: The String Catacombs

### 🔮 What is a String?

Strings are **magical sequences of runes (characters)**. They store names, spells, prophecies, and sacred messages. You can forge them using:

* `"Double quotes"`
* `'Single quotes'`
* `'''Triple quotes'''` *(for scrolls that span many lines)*

```python
scroll = "This is the hero's prophecy"
```

### 🔓 Escape Runes

Want a new line or tab in your scroll? Use these runes:

| Rune | Effect    |
| ---- | --------- |
| `\n` | New line  |
| `\t` | Tab space |

```python
scroll = "The dungeon awakens.\nPrepare yourself!"
print(scroll)
```

---

### ⚔️ String Combat Skills

#### 🔗 Concat: Merging Spells

```python
hero = "Dark"
guild = "Blade"
banner = hero + " " + guild
print(banner)  # Dark Blade
```

#### 📏 Measuring the Spell

```python
len(hero)  # 4
len(banner)  # 10
```

#### 🗺️ Rune Index Map

Every rune has a position:

```
D   a   r   k       B   l   a   d   e
0   1   2   3   4   5   6   7   8   9
```

```python
slogan = "Dark Blade"
print(slogan[0])  # D
```

#### 💀 Immutable Spells

Runes cannot be altered directly once forged.

#### 🪓 Slice and Dice

```python
title = "Dark Blade"
print(title[1:4])  # ark
print(title[:4])   # Dark
print(title[5:])   # Blade
```

#### 🧟 Negative Indexing (Backstabbing)

```
B   l   a   d   e
0   1   2   3   4
-5 -4  -3  -2  -1
```

```python
word = "Blade"
print(word[-3:-1])  # ad
```

---

### 🛠️ String Enchantments

| Spell            | Purpose                    |
| ---------------- | -------------------------- |
| `.endswith("x")` | Checks how the scroll ends |
| `.capitalize()`  | Capitalizes the first rune |
| `.replace(x, y)` | Swap runes                 |
| `.find("x")`     | Locate a rune              |
| `.count("x")`    | Count rune appearances     |

```python
scroll = "The Sorcerer of Code"
print(scroll.replace("Code", "Chaos"))  # The Sorcerer of Chaos
```

---

## 🧩 Quest 2: The Conditional Chambers

> 🗝️ "Only the adventurer with logic may unlock the gates ahead..."

### 🔥 if-elif-else Ritual

```python
if (condition):
    # success path
elif (another_condition):
    # fallback path
else:
    # default path
```

### 🧪 Mind Your Tabs

Indentation is your **shield**. Spells break without proper formation!

### 🧠 Logic Trials

#### 🚦 Signal Rune Puzzle

```python
signal = "green"

if (signal == "red"):
    print("Stop")
elif (signal == "green"):
    print("Go")
elif (signal == "yellow"):
    print("Caution")
else:
    print("Rune is broken")
```

#### 🧙 Grade Judgment Scroll

```python
marks = int(input("Reveal your marks: "))

if (marks >= 90):
    grade = "A"
elif (marks >= 80):
    grade = "B"
elif (marks >= 70):
    grade = "C"
else:
    grade = "D"

print("You have been assigned grade ->", grade)
```

---

## 🎓 Practice Scrolls of Wisdom

### 🧠 Name Length Spell

```python
name = input("Enter your title: ")
print("Length of your title is:", len(name))
```

### 💰 Count the '\$' Rune

```python
sack = "Gold hoard: $500.00 and another $700.00"
print("Count of $ is:", sack.count("$"))  # 2
```

---

## 🧪 Conditional Trials of Logic

### Q1: Odd vs Even Oracle

```python
num = int(input("Summon a number: "))
if (num % 2 == 0):
    print("EVEN")
else:
    print("ODD")
```

### Q2: Three-Number Duel

```python
a = int(input("First warrior: "))
b = int(input("Second warrior: "))
c = int(input("Third warrior: "))

if (a >= b and a >= c):
    print("Champion is:", a)
elif (b >= c):
    print("Champion is:", b)
else:
    print("Champion is:", c)
```

### Q3: Curse of Multiples

```python
x = int(input("Choose a number: "))
if (x % 7 == 0):
    print("Blessed by the Seven")
else:
    print("Not marked by the Seven")
```

---

## 🏁 Chapter Conquered

🧝 "You have emerged victorious from the String Catacombs and solved the puzzles of the Conditional Chambers. New spells await in the deeper dungeons... onward, O Hero of Code!"
