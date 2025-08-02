# 🏰 Chapter 2: The String Catacombs and Conditional Chambers

# 🧵 Quest 1: The String Catacombs

# 🔮 What is a String?
dialogue = "This is the hero's journey"

# 🔓 Escape Sequences
scroll = "The dungeon awaits.\nStep forward!"
print(scroll)

# ⚔️ String Combat Skills
# 🔗 Concatenation (Merging Spells)
hero = "Shadow"
guild = "Guild"
callout = hero + " " + guild
print(callout)  # Shadow Guild

# 📏 Measure the Magic (Length)
print(len(hero))      # 6
print(len(callout))   # 12

# 🗺️ The Map of Indexing
word = "Shadow Guild"
print(word[0])  # S

# 🪓 Slice and Dice
name = "Shadow Guild"
print(name[1:4])    # had
print(name[:4])     # Shad
print(name[7:])     # Guild

# 🧟 Negative Indexing
word = "Apple"
print(word[-3:-1])  # pl

# 🛠️ String Enchantments (Functions)
scroll = "The Wizard of Python"
print(scroll.replace("Python", "Flames"))  # The Wizard of Flames
print(scroll.endswith("Python"))           # True
print(scroll.capitalize())                 # The wizard of python
print(scroll.find("z"))                    # 6
print(scroll.count("o"))                   # 2

# 🧩 Quest 2: The Conditional Chambers

# 🔥 if-elif-else Spell Format
print("🧙‍♂️ Enter the Conditional Chambers!")
rank = input("Enter your rank (F, E, D): ").upper()
if (rank == "F"):
    print("You are a beginner in the Dungeon of DSA!")
elif (rank == "E"):
    print("You are an intermediate adventurer!")
else:
    print("You are a seasoned warrior!")

# 🧙 Grading Scroll
print("🧙‍♂️ The Grading Scroll:")
mana = int(input("Enter your mana points (0-100): "))
if (mana >= 90):
    grade = "A"
elif (mana >= 80):
    grade = "B"
elif (mana >= 70):
    grade = "C"
else:
    grade = "D"
print("Your grade is ->", grade)

# 🧠 Practice Scrolls
# Q1: Name Length Spell
print("🧙‍♂️ The Name Length Spell:")
name = input("Enter your name: ")
print("Length of your name is:", len(name))

# Q2: Count the '$' Rune
print("🧙‍♂️ The Count of the '$' Rune:")
string = "Hi, I am the $ symbol $99.99"
print("Count of $ is:", string.count("$"))  # 2

# 🧪 Conditional Trials
# Q1: Odd vs Even Oracle
print("🔮 The Odd vs Even Oracle:")
print("Enter a number to determine if it's ODD or EVEN:")
num = int(input("Enter a number: "))
if (num % 2 == 0):
    print("EVEN")
else:
    print("ODD")

# Q2: Three-Number Duel
print("⚔️ The Three-Number Duel:")
print("Enter three numbers to find the largest:")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if (a >= b and a >= c):
    print("First number is the largest:", a)
elif (b >= c):
    print("Second number is the largest:", b)
else:
    print("Third number is the largest:", c)

# Q3: Multiple of 7 Curse
print("🧙‍♂️ The Multiple of 7 Curse:")
x = int(input("Enter a number: "))
if (x % 7 == 0):
    print("Multiple of 7")
else:
    print("Not a Multiple")