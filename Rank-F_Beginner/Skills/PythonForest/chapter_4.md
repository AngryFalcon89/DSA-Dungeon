# 🧙‍♂️ Chapter 4: The Arcane Vault of Dictionaries & Sets

> 🔊 *"Beyond the Pillars of Tuples lies a chamber pulsing with mystic keys and swirling elemental glyphs. This is the Vault where secrets are paired and unique sigils gather—welcome, brave one, to the Vault of Dictionaries and the Sanctuary of Sets."*

---

## 🗝️ Quest 1: The Spellbook of Dictionaries

Dictionaries are **arcane spellbooks**, where each rune (key) holds powerful secrets (values). Use them to store mystical knowledge in a way mortals call **key-value pairs**.

---

### 📜 Crafting the Spellbook (Dictionaries)

Use curly braces `{}` to enchant your spellbook.

```python
info = {
   "key" : "value",
   "name" : "The Guild",
   "learning" : "Spellcrafting"
}
```

Keys must be **immutable** artifacts—like runes (`str`, `int`, `tuple`). Values can be of any essence—numbers, scrolls, even other spellbooks.

```python
hunter = {
   "name": "Sage Ahmad",
   "age": 22,
   "is_adult": True,
   "disciplines": ["alchemy", "combat", "lore"],
   "paths": ("dictionary", "set")
}
```

---

### 🧾 Properties of a Spellbook (Dictionaries)

* 🔀 **Unordered Scrolls**: The entries shift like illusions—no fixed order.
* ♻️ **Mutable Wisdom**: Runes and meanings can be changed or added at will.
* 🧿 **Unique Runes Only**: No duplicate keys allowed—new overwrites old.

---

### 🔍 Reading & Rewriting Spells

```python
hunter = {
   "name": "Sage Ahmad",
   "subjects": {"alchemy": 97, "combat": 98, "lore": 95}
}

print(hunter["name"])  # ✨ Reading rune

hunter["name"] = "Master Ahmad"  # ✏️ Editing spell
hunter["surname"] = "Stormblade"  # 🆕 Adding new rune
print(hunter)
```

---

### 🧩 Nested Spellbooks

When one spellbook holds another, deeper secrets can be preserved.

```python
hunter = {
   "name": "Ahmad",
   "subjects": {
      "alchemy": 97,
      "combat": 98,
      "lore": 95
   }
}

print(hunter["subjects"]["combat"])  # 🧠 98
```

---

### 🛠️ Dictionary Enchantments

* `book.keys()` → 📖 List of all runes
* `book.values()` → 💎 List of all magical essences
* `book.items()` → 🧱 All rune-essence bindings as relics
* `book.get("rune")` → 🧭 Safer way to locate a spell (returns `None` if absent)
* `book.update(new_scroll)` → 🌀 Merges new runes into the existing tome

```python
print(hunter.keys())
print(hunter.values())
print(hunter.get("name"))
print(hunter.get("guild"))  # Returns None
hunter.update({"city": "Eldoria", "rank": "Novice"})
print(hunter)
```

---

## 🔮 Quest 2: The Sanctuary of Sets

Sets are **elemental circles of power**, holding only **unique sigils**. These are raw, unordered sources of energy.

---

### 🔥 Conjuring a Set

```python
sigils = {1, 2, 3, 4, 2, "fire", "wind", "wind"}
print(sigils)  # Duplicates vanish like mist
print(type(sigils))  # <class 'set'>
print(len(sigils))  # Number of unique sigils
```

Use `set()` for an empty ritual circle.

```python
empty_circle = set()
```

---

### ⚖️ Set Laws

* 🎯 Only **immutable** artifacts allowed.
* ♻️ The circle itself is **mutable**—you can summon or banish sigils.
* 🔀 No order, no index—only essence.

---

### 🛠️ Set Rituals

* `sigils.add(x)` → 🔥 Add rune
* `sigils.remove(x)` → ❌ Banish (error if absent)
* `sigils.clear()` → 🌫 Empty the circle
* `sigils.pop()` → 🌀 Randomly sacrifice one
* `set1.union(set2)` → 🤝 Merge two powers
* `set1.intersection(set2)` → 🎯 Find common sigils

```python
circle1 = {1, 2, 3}
circle2 = {2, 3, 4}

print(circle1.union(circle2))  # {1, 2, 3, 4}
print(circle1.intersection(circle2))  # {2, 3}
```

---

## 📜 Practice Scrolls

---

### 🎯 Q1: Runebook of Word Meanings

```python
rune_book = {
    "cat": "a small beast of stealth",
    "table": ["a sacred resting surface", "scroll of structured facts"]
}

print(rune_book)
```

---

### 🧮 Q2: Classroom Sigil Counter

```python
subjects = {"alchemy", "combat", "curses", "alchemy", "runes", "combat", "alchemy", "combat", "curses", "enchantment"}
unique_classrooms = len(subjects)
print("🏫 Number of classrooms needed:", unique_classrooms)  # Output: 5
```

---

### ✍️ Q3: Marking Spell Registry

```python
marks = {}

alchemy = int(input("Enter marks for Alchemy: "))
marks.update({"alchemy": alchemy})

combat = int(input("Enter marks for Combat: "))
marks.update({"combat": combat})

lore = int(input("Enter marks for Lore: "))
marks.update({"lore": lore})

print("📖 Marks Registry:", marks)
```

---

### 🎭 Q4: Sigil Separation Challenge

Python treats `9` and `9.0` as identical glyphs—but we must **distinguish** them in the circle.

```python
sigils = {
    ("int", 9),
    ("float", 9.0)
}

print("⚔️ Unique Sigils:", sigils)
```

---

## 🏁 Chapter Complete

> 🧙 "You have uncovered the arcane mechanics of dictionaries and the raw energies of sets. The next trial awaits in the **Looping Labyrinth**, where time and repetition serve your will..."

---