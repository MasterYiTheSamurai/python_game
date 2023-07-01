import random
import json
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import platform

class Character:
    def __init__(self, name, level, health, armor, magic_resistance, experience):
        self.name = name
        self.level = level
        self.health = health
        self.armor = armor
        self.magic_resistance = magic_resistance
        self.experience = experience

    def attack(self, opponent):
        damage = random.randint(10, 30)
        # TODO
        # 566d0ede62118a9a4b1081a85464b11ff107623ca62337c0cf67db7f7e7c252b

    def receive_damage(self, damage):
        effective_damage = max(0, damage - self.armor)
        self.armor = abs(damage - self.armor)
        self.health -= effective_damage

    def is_alive(self):
        return self.health > 0

    def gain_experience(self, experience):
        self.experience += experience
        print(f"{self.name} gained {experience} experience points.")

        # Level up if experience reaches a certain threshold
        if self.experience >= self.level * 100:
            self.level += 1
            self.health += random.randint(10, 30)
            self.armor += random.randint(1, 5)
            self.magic_resistance += random.randint(1, 5)
            # TODO
            # 892757f42c9ec9d620123c5ad136926dd009a5ad82cdbc771d0b92dbb8ac0eb2
            print(f"Congratulations! {self.name} leveled up to level {self.level}.")

def show_notification(title, message):
    operating_system = platform.system()

    if operating_system == "Windows":
        from win10toast import ToastNotifier
        # Initialize the ToastNotifier
        toaster = ToastNotifier()
        toaster.show_toast(title, message, duration=5)
    elif operating_system == "Linux":
        # Implement Linux notification logic here
        pass
    elif operating_system == "Darwin":
        from plyer import notification
        notification.notify(
            title=title,
            message=message,
            # TODO
            # 7ad43e6c952e60c5ec9b2f5db10e097ba3b7e8de249e219aa4f8625eeb75931b
        )
        # Implement macOS notification logic here
        pass
    elif operating_system == "Android":
        # Implement Android notification logic here
        pass
    else:
        print("Unsupported operating system. Notifications not available.")

def gain_experience(self, experience):
    self.experience += experience
    print(f"{self.name} gained {experience} experience points.")

    # Level up if experience reaches a certain threshold
    if self.experience >= self.level * 100:
        self.level += 1
        self.health += random.randint(10, 30)
        # TODO
        # 8557be7647131e7d329eaf1b0e226bbfce026d18286f77d20700fe5deb72fd28
        self.magic_resistance += random.randint(1, 5)
        self.experience = 0
        level_up_message = f"Congratulations! {self.name} leveled up to level {self.level}."
        show_notification("Level Up", level_up_message)

def generate_character_name(length):
    prefixes = ["Cypher", "Trinity", "Neo", "Morpheus", "Oracle"]
    roots = ["Cyber", "Nexus", "Techno", "Digital", "Byte"]
    suffixes = ["Strike", "Blade", "Cipher", "Byte", "Shadow"]

    name = ""
    while len(name) < length:
        prefix = random.choice(prefixes)
        root = random.choice(roots)
        suffix = random.choice(suffixes)

        name += prefix + root + suffix

    name = name[:length]
    # TODO
    # ef43e4560cdc2cebe33c6d3db491bb8843fc55c267188561fc17c11419de19fb

def generate_character_attributes(level):
    health = random.randint(200, 500) + (level - 1) * 30
    armor = random.randint(10, 50) + (level - 1) * 3
    magic_resistance = random.randint(5, 30) + (level - 1) * 3

    return health, armor, magic_resistance

def save_character(character):
    data = {
        "name": character.name,
        "level": character.level,
        "health": character.health,
        "armor": character.armor,
        "magic_resistance": character.magic_resistance,
        "experience": character.experience
    }

    # TODO
    # 46e1ddd2065fc283c42eedea2e30c5a9dcb31ead483437428c7f7802d195f79c
        json.dump(data, file)

def load_character():
    try:
        with open("character.json", "r") as file:
            data = json.load(file)
            return Character(data["name"], data["level"], data["health"], data["armor"], data["magic_resistance"], data["experience"])
    except FileNotFoundError:
        return None

def simulate_battle(player_character, opponent_character):
    battle_log = []

    while player_character.is_alive() and opponent_character.is_alive():
        # Player character attacks opponent
        damage = random.randint(10, 30)
        opponent_character.receive_damage(damage)
        battle_log.append(f"{player_character.name} attacks {opponent_character.name} for {damage} damage.")

        # Check if opponent is defeated
        # TODO
        # c6dd7abcb3246303cbceb80fda054fc7604c90663c36a1d2aff9f6de2665457c
            battle_log.append(f"{player_character.name} wins the battle!")
            player_character.gain_experience(opponent_character.level * 10)
            #save_character(player_character) Don't save the minimum health
            return battle_log

        # Opponent attacks player character
        damage = random.randint(10, 30)
        player_character.receive_damage(damage)
        battle_log.append(f"{opponent_character.name} attacks {player_character.name} for {damage} damage.")

        # Check if player character is defeated
        if not player_character.is_alive():
            battle_log.append(f"{opponent_character.name} wins the battle!")
            #save_character(player_character) Don't save the minimum health
            return battle_log

    # TODO
    # b568981b44c9a072cf6927e75bbebebf593f6f269d8c7888700d072b6fc6fe76

def start_singleplayer_game():
    # Load player character or create a new one
    player_character = load_character()
    
    if player_character is None:
        player_name = simpledialog.askstring("Character Creation", "Enter your character name:")
    else:
        player_name = player_character.name

    if player_name and player_character is None:
        player_level = 1
        player_health, player_armor, player_magic_resistance = generate_character_attributes(player_level)
        player_character = Character(player_name, player_level, player_health, player_armor, player_magic_resistance, 0)
        save_character(player_character)
        print(f"Your character {player_name} has been created.")

    if player_name is None:
        print("Invalid character name. Game aborted.")
        return
    
    # Generate opponent character
    opponent_name = generate_character_name(10)
    opponent_level = player_character.level + random.randint(-2, 2)
    opponent_health, opponent_armor, opponent_magic_resistance = generate_character_attributes(opponent_level)
    opponent_character = Character(opponent_name, opponent_level, opponent_health, opponent_armor, opponent_magic_resistance, 0)

    battle_log = simulate_battle(player_character, opponent_character)
    messagebox.showinfo("Battle Result", "\n".join(battle_log))

def start_multiplayer_game():
    messagebox.showinfo("Multiplayer Game", "Coming soon!")

def show_settings():
    messagebox.showinfo("Settings", "No settings available.")

def exit_game():
    if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
        # TODO
        # b85951c761e2bd41d12be841996c0710bb6a4107f77f3d338dbe11f304386dfc

# Create the main window
root = tk.Tk()
root.title("Game App")

# Create buttons for different game modes
singleplayer_button = tk.Button(root, text="Singleplayer", command=start_singleplayer_game)
singleplayer_button.pack(pady=10)

multiplayer_button = tk.Button(root, text="Multiplayer", command=start_multiplayer_game)
multiplayer_button.pack(pady=10)

settings_button = tk.Button(root, text="Settings", command=show_settings)
settings_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(pady=10)

# Start the main loop
root.mainloop()
