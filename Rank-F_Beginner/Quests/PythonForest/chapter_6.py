# 🕵️‍♂️ Chapter 6: Arcana of Functions & Recursion

# 🌟 Why Bind Logic in Functions?

# Without a function
print(5 + 10)
print(12 + 17)

# With a function
def cast_sum_spell(a, b):
    print(a + b)

cast_sum_spell(5, 10)
cast_sum_spell(12, 17)

# ✨ The Ritual of Declaration
def calculate_sum(a, b):
    return a + b

print(calculate_sum(5, 10))

# 🪧 Default Spell Components
def cast_blade(a, b=2):
    return a * b

print(cast_blade(5))    # Uses default
print(cast_blade(3, 4)) # Uses both

# ✍️ Practice Scrolls (Function Trials)

# ✅ Trial 1: Length of a Mystic List
def spell_length(l):
    print(len(l))

spell_length(["fire", "ice", "wind"])

# ✅ Trial 2: Speak All Relics in Line
def chant_items(l):
    for item in l:
        print(item, end=" ")

chant_items(["wand", "sword", "shield"])
print()  # for newline

# ✅ Trial 3: Factorial Rune
def factorial_rune(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_rune(5))

# ✅ Trial 4: Currency Conversion Sigil
def convert_gold(usd):
    print(usd, "USD =", usd * 83, "INR")

convert_gold(100)

# 🧩 Recursion: The Infinity Loop Rune

# Recursive Countdown
def countdown(n):
    if n == 0:
        return
    print(n)
    countdown(n - 1)

countdown(5)

# 🔄 Factorial by Recursive Sigil
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# ✍️ Practice Scrolls (Recursive Trials)

# ✅ Trial 1: Sum of `n` Numbers
def calc_sum(n):
    if n == 0:
        return 0
    return n + calc_sum(n - 1)

print(calc_sum(5))

# ✅ Trial 2: Print List Recursively
def echo_list(l, idx=0):
    if idx == len(l):
        return
    print(l[idx])
    echo_list(l, idx + 1)

echo_list(["potion", "scroll", "elixir"])