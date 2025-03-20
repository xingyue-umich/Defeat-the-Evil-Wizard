# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit
        self.evadeNextAttack = False

    def attack(self, opponent):
        if not opponent.evadeNextAttack:
            # opponent does not avoid the attack
            opponent.health -= self.attack_power
            print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
            if opponent.health <= 0:
                print(f"{opponent.name} has been defeated!")
        else:
            # opponent avoid the attack
            print(f"{self.name} attacks {opponent.name} but {opponent.name} avoid it!")
            
    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")

    # Add your heal method here
    def heal(self):
        self.health = self.max_health
        print(f"{self.name} heals to {self.health} health!")


# Warrior class (inherits from Character)
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)  # Boost health and attack power

    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Power Strike")
        print("2. Siphoing Strikes")

        action = input("Which ability do you want to use? (1/2): ")

        if action == "1":
            # Power Strike: double damage attack
            damage = self.attack_power * 2
            opponent.health -= damage
            print(f"\n{self.name} performs a POWER STRIKE on {opponent.name}, dealing {damage} damage!")
            print(f"{opponent.name}'s health is now {opponent.health}.")
        elif action == "2":
            # Siphoing Strikes: strikes the opponents and heals for the half damage dealt
            opponent.health -= self.attack_power
            self.health += (self.max_health - self.health) // 2
            print(f"\n{self.name} attacks the {opponent.name}, and heals to {self.health}")
            print(f"{opponent.name}'s health is now {opponent.health}.")
        else:
            print("\nInvalid input! No ability used.")


# Mage class (inherits from Character)
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)  # Boost attack power

    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Fireball")
        print("2. Mana Shield")

        action = input("Which ability do you want to use? (1/2): ")

        if action == "1":
            # Fireball: high damage attack
            damage = self.attack_power + 20  # Extra damage on top of the Mage's attack power
            opponent.health -= damage
            print(f"\n{self.name} casts FIREBALL at {opponent.name}, dealing {damage} damage!")
            print(f"{opponent.name}'s health is now {opponent.health}.")
        elif action == "2":
            # Mana Shield: avoid next damage
            self.evadeNextAttack = True
            print(f"\n{self.name} activates MANA SHIELD and will avoid the next attack!")
        else:
            print("\nInvalid input! No ability used.")

# Archer class (inherits from Character)
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=50)
    
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Quick Shot")
        print("2. Evade")
        
        action = input("Which ability do you want to use? (1/2): ")
        
        if action == "1":
            # Quick shot
            damage = self.attack_power * 2
            opponent.health -= damage
            print(f"\n{self.name} double the attack of their arrows to {damage}")
            print(f"{opponent.name}'s health is now {opponent.health}.")
        elif action == "2":
            # Avoid next attack
            self.evadeNextAttack = True
            print(f"\n{self.name} will avoid the next attack from {opponent.name}")
        else:
            print("\nInvalid input! No ability used.")
        
# Paladin class (inherits from Character)
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=200, attack_power=20)
        
    def special_ability(self, opponent):
        print("\nAbilities:")
        print("1. Holy Strike")
        print("2. Divine Shield")
        
        action = input("Which ability do you want to use? (1/2): ")
        
        if action == "1":
            # Holy Strike increases attack power by 30
            damage = self.attack_power + 30
            opponent.health -= damage
            print(f"\n{self.name} increase the attack of their damage to {damage}")
            print(f"{opponent.name}'s health is now {opponent.health}.")
        elif action == "2":
            # Block the next attack and increase 10 health
            self.evadeNextAttack = True
            self.health += 10
            if self.health > self.max_health:
                self.health = self.max_health
            print(f"\n{self.name} will block the next attack from {opponent.name}")
        else:
            print("\nInvalid input! No ability used.")
        

# EvilWizard class (inherits from Character)
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)  # Lower attack power
    
    # Evil Wizard's special ability: it can regenerate health
    def regenerate(self):
        self.health += 5  # Lower regeneration amount
        print(f"{self.name} regenerates 5 health! Current health: {self.health}")
