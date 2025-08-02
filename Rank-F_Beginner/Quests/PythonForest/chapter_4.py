# 🧙‍♂️ Chapter 4: The Arcane Vault of Dictionaries & Sets

# Quest 1: The Spellbook of Dictionaries

# Crafting the Spellbook
info = {
    "key": "value",
    "name": "The Guild",
    "learning": "Spellcrafting"
}

hunter = {
    "name": "Sage Ahmad",
    "age": 22,
    "is_adult": True,
    "disciplines": ["alchemy", "combat", "lore"],
    "paths": ("dictionary", "set")
}

# Properties and Manipulations
hunter = {
    "name": "Sage Ahmad",
    "subjects": {"alchemy": 97, "combat": 98, "lore": 95}
}

# Reading rune
print("✨", hunter["name"])

# Editing spell
hunter["name"] = "Master Ahmad"

# Adding new rune
hunter["surname"] = "Stormblade"
print(hunter)

# Nested Spellbook
hunter = {
    "name": "Ahmad",
    "subjects": {
        "alchemy": 97,
        "combat": 98,
        "lore": 95
    }
}
print("🧠", hunter["subjects"]["combat"])

# Dictionary Enchantments
print("📖", hunter.keys())
print("💎", hunter.values())
print("🧭", hunter.get("name"))
print("🧭 (missing)", hunter.get("guild"))  # Returns None
hunter.update({"city": "Eldoria", "rank": "Novice"})
print("🌀", hunter)

# Quest 2: The Sanctuary of Sets

# Conjuring a Set
sigils = {1, 2, 3, 4, 2, "fire", "wind", "wind"}
print("✨ Unique Sigils:", sigils)
print("🔍 Type:", type(sigils))
print("📏 Count:", len(sigils))

# Empty ritual circle
empty_circle = set()

# Set Rituals
circle1 = {1, 2, 3}
circle2 = {2, 3, 4}
print("🤝 Union:", circle1.union(circle2))
print("🎯 Intersection:", circle1.intersection(circle2))

# Practice Scrolls

# Q1: Runebook of Word Meanings
rune_book = {
    "cat": "a small beast of stealth",
    "table": ["a sacred resting surface", "scroll of structured facts"]
}
print("📖 Rune Book:", rune_book)

# Q2: Classroom Sigil Counter
subjects = {"alchemy", "combat", "curses", "alchemy", "runes", "combat", "alchemy", "combat", "curses", "enchantment"}
unique_classrooms = len(subjects)
print("🏫 Number of classrooms needed:", unique_classrooms)

# Q3: Marking Spell Registry
marks = {}
alchemy = int(input("Enter marks for Alchemy: "))
marks.update({"alchemy": alchemy})

combat = int(input("Enter marks for Combat: "))
marks.update({"combat": combat})

lore = int(input("Enter marks for Lore: "))
marks.update({"lore": lore})

print("📖 Marks Registry:", marks)

# Q4: Sigil Separation Challenge
sigils = {
    ("int", 9),
    ("float", 9.0)
}
print("⚔️ Unique Sigils:", sigils)
