# Filename: q1_sg5_a1_Arayat_Martinez.py

class Hero:
    def __init__(self, name, hp):
        # Define: Initialize attributes for name and hp
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        # Act: Subtract damage amount from current hp
        self.hp -= amount
        print(f"{self.name} took {amount} damage! Remaining HP: {self.hp}")

# Instantiate: Create two heroes
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

print(f"Initial HP - {arthur.name}: {arthur.hp}, {morgana.name}: {morgana.hp}\n")

# Make Arthur take 10 damage
arthur.take_damage(10)

# Print both HPs to verify Morgana was unaffected
print("\n--- Final Status ---")
print(f"{arthur.name}'s HP: {arthur.hp}")
print(f"{morgana.name}'s HP: {morgana.hp}")
