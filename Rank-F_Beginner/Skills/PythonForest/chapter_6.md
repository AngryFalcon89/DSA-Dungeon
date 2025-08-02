# 🕵️‍♂️ Chapter 6: Arcana of Functions & Recursion

> 🎧 *"Beyond the Labyrinth of Loops lies the Tower of Spellcraft, where ancient scrolls reveal the art of modular incantations. Here, adventurer, you shall uncover the sacred magic of **functions** and the recursive rune loops that summon infinite power..."*

---

## 📜 The Spell of Function

A **function** is a reusable magical glyph—a block of code that performs a specific task. You've already conjured built-in scrolls like `print()` and `len()`. Now, you forge your own.

### 🌟 Why Bind Logic in Functions?

Without a function:

```python
# Cast spell twice
print(5 + 10)
print(12 + 17)
```

With a function:

```python
def cast_sum_spell(a, b):
    print(a + b)

cast_sum_spell(5, 10)
cast_sum_spell(12, 17)
```

🕉 More readable, reusable, and power-efficient spellcraft!

### ✨ The Ritual of Declaration

```python
def calculate_sum(a, b):  # ritual defines parameters
    return a + b           # enchanted output

print(calculate_sum(5, 10))  # invocation with arguments
```

#### 📙 Function Scroll Terminology

* **Function Definition**: Starts with `def`
* **Function Call**: Spell invocation
* **Parameters**: Variables in the glyph
* **Arguments**: Actual spell inputs
* **`return`**: Sends enchanted result back

### ⚔️ Types of Function Scrolls

1. **Built-In Spells**: `print()`, `len()`
2. **Custom Scrolls**: Forged by adventurers like you

### 🪧 Default Spell Components

```python
def cast_blade(a, b=2):
    return a * b

cast_blade(5)    # Uses default
cast_blade(3, 4) # Uses both
```

---

## ✍️ Practice Scrolls (Function Trials)

### ✅ Trial 1: Length of a Mystic List

```python
def spell_length(l):
    print(len(l))

spell_length(["fire", "ice", "wind"])
```

### ✅ Trial 2: Speak All Relics in Line

```python
def chant_items(l):
    for item in l:
        print(item, end=" ")

chant_items(["wand", "sword", "shield"])
```

### ✅ Trial 3: Factorial Rune

```python
def factorial_rune(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_rune(5))
```

### ✅ Trial 4: Currency Conversion Sigil

```python
def convert_gold(usd):
    print(usd, "USD =", usd * 83, "INR")

convert_gold(100)
```

---

## 🧩 Recursion: The Infinity Loop Rune

> ⚠️ *Warning: Forbidden knowledge. Recursion is powerful and must be handled with care!*

**Recursion** is when a spell calls itself to break a mighty challenge into smaller trials.

### 🧹 The Recursive Code Circle

1. **Base Case**: Ending point
2. **Recursive Step**: Spell continues

```python
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

### 🔄 Factorial by Recursive Sigil

```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

---

## ✍️ Practice Scrolls (Recursive Trials)

### ✅ Trial 1: Sum of `n` Numbers

```python
def calc_sum(n):
    if n == 0:
        return 0
    return n + calc_sum(n - 1)

print(calc_sum(5))
```

### ✅ Trial 2: Print List Recursively

```python
def echo_list(l, idx=0):
    if idx == len(l):
        return
    print(l[idx])
    echo_list(l, idx + 1)

echo_list(["potion", "scroll", "elixir"])
```

---

## 🔮 Chapter Complete

> 💜 *You now wield the twin tomes of Function and Recursion! The next path awaits in the Realm of Advanced Spells...*

---