# 🏰 Chapter 3: The Vault of Lists & Tuples
# 👣 Quest Start: Enter the enchanted domain of scrolls and immutable relics.

# 🔢 Quest 1: The Scrolls of Lists

print("📜 Forging the List Scroll:")
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print("🔮 Marks:", marks)
print("🏷️ Type of marks:", type(marks))  # <class 'list'>

print("\n🛍️ List Traits & Index Magic:")
student = ["Hunter Bilal", 95, "Weakest Hunter of all time"]
print("🎒 Student Scroll:", student)

print("\n⚙️ Activating Mutability Charm:")
student[1] = 97
print("🧠 Upgraded Stats:", student)

print("\n🔍 Slice and Scry Activated:")
marks = [85, 94, 76, 63, 48]
print("🔪 Sliced [1:4]:", marks[1:4])  # [94, 76, 63]
print("🔪 Sliced [-3:-1]:", marks[-3:-1])  # [76, 63]

# 🔧 Enchantments: List Methods
print("\n🔧 Spellcasting List Methods:")
inventory = ["sword", "potion"]
inventory.append("shield")
inventory.sort()
print("🎒 Sorted Inventory:", inventory)

# 🏛️ Quest 2: The Pillars of Tuples

print("\n🏛️ Conjuring Tuple Relic:")
tup = (94.4, 87.5, 95.2)
print("📜 Tuple Relic:", tup)

print("\n🚫 Attempt to Break the Immutable Edict:")
try:
    tup[0] = 5  # Forbidden!
except TypeError as e:
    print("❌ Error:", e)

print("\n🔍 Scrying Tuple Energies:")
tup = (1, 2, 3, 2)
print("🔎 Index of '2':", tup.index(2))  # 1
print("📊 Count of '2':", tup.count(2))  # 2

# 🌟 Practice Scrolls

print("\n🎬 Practice Scroll Q1: Favorite Memory Scrolls")
skill = []
for i in range(3):
    skill.append(input(f"Enter favorite skill {i+1}: ")) 
print("📼 Your favorite skill:", skill)

print("\n⚔️ Practice Scroll Q2: Palindrome Rune Test")
list1 = [1, 2, 3, 2, 1]
if list1 == list1[::-1]:
    print("🌟 Palindrome Scroll!")
else:
    print("❌ Not a Palindrome")

print("\n📙 Practice Scroll Q3: Grade Count Incantation")
grades = ("C", "D", "A", "A", "B", "B", "A")
print("'A' runes counted:", grades.count("A"))  # 3

print("\n🌟 Practice Scroll Q4: Sort the Grade Relics")
grades_list = ["C", "D", "A", "A", "B", "B", "A"]
grades_list.sort()
print("📚 Sorted grades:", grades_list)  # ['A', 'A', 'A', 'B', 'B', 'C', 'D']

# 🏁 Chapter Conclusion
print("\n🏁 Quest Complete: Vault of Lists & Tuples conquered!")
print("🎯 Prepare for your next quest: The Looping Labyrinth...")
