# Filename: q1_sg5_a1_Arayat_Martinez.py

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount
        print(f"{self.name} took {amount} damage! Remaining HP: {self.hp}")


arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

print(f"Initial HP - {arthur.name}: {arthur.hp}, {morgana.name}: {morgana.hp}\n")


arthur.take_damage(10)


print("\n--- Final Status ---")
print(f"{arthur.name}'s HP: {arthur.hp}")
print(f"{morgana.name}'s HP: {morgana.hp}")
