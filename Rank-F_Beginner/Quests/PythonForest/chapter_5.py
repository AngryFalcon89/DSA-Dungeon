# 🕵️‍♂️ Chapter 5: The Looping Labyrinth

# ⏳ `while` Loop: The Temporal Chant
print("🔮 Temporal Chant Demo")
count = 1
while count <= 5:
    print("🔮 Hello, adventurer!")
    count += 1

# 🚨 Infinite Chanting (Do not run!)
# while True:
#     print("♻️ Chanting forever...")

# ⚔️ Practice Scrolls: `while` Loop

# ✅ Quest 1: Print 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# ❌ Quest 2: Print 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# 🌊 Quest 3: Multiplication Spell
n = int(input("Enter number for multiplication table: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# 🛠️ Quest 4: Traverse the Sigil List
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1

# 🔀 Loop Control Runes

# ❌ `break` - Escape Portal
nums = (1, 4, 9, 16, 36, 49)
x = 36
i = 0
while i < len(nums):
    if nums[i] == x:
        print("✨ Found at", i)
        break
    i += 1

# ⏭️ `continue` - Skip Chant
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# 🧙‍♂️ `for` Loop: Spirit Walker
veggies = ["potato", "brinjal", "ladyfinger"]
for veg in veggies:
    print(veg)

word = "Dungeon"
for ch in word:
    print(ch)

# 📆 `else` in Loops
for ch in "Dungeon":
    if ch == 'o':
        break
else:
    print("✅ End of sequence")

# ⏱ `range()` Function: Time Gate Generator
for i in range(5):
    print(i)

for i in range(2, 5):
    print(i)

for i in range(2, 10, 2):
    print(i)

# 🔢 Practice Scrolls: `for` + `range()`

# 1. Numbers 1 to 100
for i in range(1, 101):
    print(i)

# 2. Numbers 100 to 1
for i in range(100, 0, -1):
    print(i)

# 3. Multiplication Spell
n = int(input("Enter number for multiplication (for loop): "))
for i in range(1, 11):
    print(n * i)

# 🏛 `pass` Spell: Null Incantation
for i in range(5):
    pass  # Placeholder rune

print("Work continues...")

# 🪄 Final Challenges

# 🔢 Sum of first `n` natural numbers (while)
n = 5
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print("Total sum =", sum)

# 🪩 Factorial of `n` (for)
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial =", fact)