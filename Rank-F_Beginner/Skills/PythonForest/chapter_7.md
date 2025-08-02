# 🕵️ Chapter 7: The Chamber of Eternal Scrolls (File I/O)

> 🎧 *"Beyond the recursion gates lies the Chamber of Eternal Scrolls. Here, adventurers learn to scribe, summon, and banish runes upon the ancient scrolls of memory..."*

---

## 🔬 Why Do Scrolls Matter?

When you cast spells in Python, your runes live in volatile RAM. But once the power fades (or your device shuts down), so do your incantations.

Thus, we etch our knowledge into **eternal scrolls** (files) that survive the night.

---

## 📄 Types of Magical Scrolls

1. **Text Scrolls** (`.txt`, `.py`): Glyphs and readable runes
2. **Binary Scrolls** (`.png`, `.mp4`): Dark magic encoded in bytes

We focus on the scrolls of light — the **text scrolls**.

---

## 🖊️ Spellbinding a Scroll: Opening Files

```python
f = open("scroll.txt", "r")  # Opens scroll in Read Mode
```

### 🔐 Scroll Modes:

| Mode | Purpose                                 |
|------|-----------------------------------------|
| `r`  | Read existing scroll                     |
| `w`  | Write (overwrites scroll)               |
| `a`  | Append new runes to the scroll's end    |
| `x`  | Create new scroll (error if exists)     |
| `+`  | Combine read/write (`r+`, `w+`, etc.)   |

> 💚 Tip: Add `b` (like `rb`, `wb`) to conjure binary scrolls.

---

## 📝 Reading the Scrolls

```python
f = open("scroll.txt", "r")
data = f.read()        # Read entire scroll
line = f.readline()   # Read one incantation (line)
f.close()
```

---

## 🌟 Writing or Enhancing a Scroll

```python
# 🔪 Rewriting scroll
f = open("scroll.txt", "w")
f.write("Let the fire rise!\n")
f.close()

# 🌊 Adding to the end
f = open("scroll.txt", "a")
f.write("A new spell emerges...\n")
f.close()
```

---

## 🧡 The "with" Ritual: Safe Casting

```python
with open("scroll.txt", "r") as f:
    data = f.read()
    print(data)
# 🌟 Auto-closes the scroll safely
```

---

## 💣 Destroying a Cursed Scroll

```python
import os
os.remove("dark_scroll.txt")
```

---

## 🎓 Spell Trials (Practice Scrolls)

### ✅ Trial 1: Craft a Scroll with Chants

```python
with open("practice.txt", "w") as f:
    f.write("Hi everyone\n")
    f.write("we are learning File I/O\n")
    f.write("using Python.\n")
    f.write("I like programming in Python.")
```

### ✅ Trial 2: Transmute Word of Power

```python
def replace_word():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Java", "Python")

    with open("practice.txt", "w") as f:
        f.write(new_data)
```

### ✅ Trial 3: Rune Discovery

```python
word_to_find = "learning"

with open("practice.txt", "r") as f:
    data = f.read()
    if word_to_find in data:
        print("🕵️ Rune Found")
    else:
        print("❌ Rune Not Found")
```

### ✅ Trial 4: Where Lies the Rune?

```python
def find_line_number():
    word = "learning"
    line_num = 1
    with open("practice.txt", "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            if word in line:
                print("📅 Rune found on line:", line_num)
                return
            line_num += 1
    print("⛔ Rune not found")
```

### ✅ Trial 5: Count Even Runes

File content: `1,2,45,66,84,91,90`

```python
count = 0
with open("numbers.txt", "r") as f:
    data = f.read()
    nums = data.split(",")
    for n in nums:
        if int(n) % 2 == 0:
            count += 1
print("Even runes:", count)
```

---

## 🔺 Chapter Complete

> 🧙 "The Chamber of Eternal Scrolls bends to your will now. The next trial lies within the Forest of Object Shadows, where Classes walk as living spells..."

---
