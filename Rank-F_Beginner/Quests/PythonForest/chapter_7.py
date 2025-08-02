# 🕵️ Chapter 7: The Chamber of Eternal Scrolls (File I/O)

# 🔍 Trial 1: Craft a Scroll with Chants
def inscribe_scroll():
    with open("practice.txt", "w") as f:
        f.write("Hi everyone\n")
        f.write("we are learning File I/O\n")
        f.write("using Python.\n")
        f.write("I like programming in Python.")

# 🔍 Trial 2: Transmute Word of Power
def replace_word():
    with open("practice.txt", "r") as f:
        data = f.read()

    new_data = data.replace("Java", "Python")

    with open("practice.txt", "w") as f:
        f.write(new_data)

# 🔍 Trial 3: Rune Discovery
def search_rune(word_to_find="learning"):
    with open("practice.txt", "r") as f:
        data = f.read()
        if word_to_find in data:
            print("🕵️ Rune Found")
        else:
            print("❌ Rune Not Found")

# 🔍 Trial 4: Where Lies the Rune?
def find_rune_line(word="learning"):
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

# 🔍 Trial 5: Count Even Runes
def count_even_runes():
    count = 0
    with open("numbers.txt", "r") as f:
        data = f.read()
        nums = data.split(",")
        for n in nums:
            if int(n) % 2 == 0:
                count += 1
    print("Even runes:", count)

# 🪄 Bonus Spell: Destroying a Cursed Scroll
def destroy_scroll(filename):
    import os
    try:
        os.remove(filename)
        print(f"💀 {filename} has been banished.")
    except FileNotFoundError:
        print("⚠️ No such cursed scroll exists.")

# ✨ Safe Reading Ritual
def safe_cast_scroll(filename):
    try:
        with open(filename, "r") as f:
            data = f.read()
            print("🔮 Scroll reads:\n", data)
    except FileNotFoundError:
        print("⚠️ Scroll does not exist.")

# 🧪 Test spells below as needed
if __name__ == "__main__":
    inscribe_scroll()
    replace_word()
    search_rune()
    find_rune_line()
    count_even_runes()
    safe_cast_scroll("practice.txt")
    destroy_scroll("dark_scroll.txt")