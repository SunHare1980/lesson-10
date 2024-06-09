import random

class Hero:
    def __init__(self, name, health = 100, attack_power = 20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} - Здоровье: {self.health}, Сила атаки: {self.attack_power}"

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Игра началась!")
        print(self.player)
        print(self.computer)
        print()

        while self.player.is_alive() and self.computer.is_alive():
            self.player_turn()
            if not self.computer.is_alive():
                break
            self.computer_turn()

        if self.player.is_alive():
            print(f"{self.player.name} победил!")
        else:
            print(f"{self.computer.name} победил!")

    def player_turn(self):
        print("Ход игрока!")
        self.player.attack(self.computer)
        print(self.computer)
        print()

    def computer_turn(self):
        print("Ход компьютера!")
        self.computer.attack(self.player)
        print(self.player)
        print()

if __name__ == "__main__":
    player_hero = Hero(name="Игрок")
    computer_hero = Hero(name="Компьютер")

    game = Game(player=player_hero, computer=computer_hero)
    game.start()