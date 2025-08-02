# 🏰 Chapter 9: Inheritance, Polymorphism & Forbidden Powers

# 💀 The `del` Curse
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Shraddha")

# Ancient deletion spell
# del s1.name
# del s1


# 🔒 Private Attributes & Shadow Spells
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass  # Hidden scroll

    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345", "abcde")
print(acc1.acc_no)         # ✅ Allowed
# acc1.__acc_pass          # ❌ Forbidden
acc1.reset_pass()          # ✅ Allowed


# 🧬 Inheritance: The Bloodline of Code
# 🐣 Single Inheritance
class Car:
    @staticmethod
    def start():
        print("Car started...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("Fortuner")
car1.start()  # 🔥 Inherited power


# 🧙 Multi-level Inheritance
class A:
    varA = "Runes of A"
class B(A):
    varB = "Sigils of B"
class C(B):
    varC = "Glyphs of C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)


# 🕸️ Multiple Inheritance
class D:
    varD = "Runes of D"
class E:
    varE = "Sigils of E"
class F(D, E):
    varF = "Glyphs of F"

f1 = F()
print(f1.varD)
print(f1.varE)


# 🪜 `super()`: Summon the Ancestor
class BasicCar:
    def __init__(self, type):
        self.type = type

class ElectricCar(BasicCar):
    def __init__(self, name, type):
        super().__init__(type)
        self.name = name

car2 = ElectricCar("Prius", "Electric")
print(car2.type)


# 🕯️ Class Methods: Alters of the Bloodline
class Person:
    name = "anonymous"

    @classmethod
    def change_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("Rahul Kumar")
print(p1.name)
print(Person.name)


# 🧾 Property Scrolls (`@property`)
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(98, 97, 99)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)


# 🧙‍♂️ Polymorphism: The Many-Faced Glyph
print(1 + 2)               # ➜ 3
print("Hi" + "There")      # ➜ HiThere
print([1, 2] + [3, 4])     # ➜ [1, 2, 3, 4]


# ✨ Operator Overloading with Dunder Spells
class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price

order1 = Order("Chips", 20)
order2 = Order("Tea", 15)
print(order1 > order2)  # 🔥 True