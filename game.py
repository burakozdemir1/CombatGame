import time
import random
import sys


class Player():
    def __init__(self, name, health=5, energy=100):
        self.name = name
        self.hit = 0
        self.health = health
        self.energy = energy

    def display_current_state(self):
        print("Hit:", self.hit)
        print("Health:", self.health)
        print("Energy:", self.energy)

    def attack(self, opponent):
        print("You performed an attack.")
        print("Attack in progress. Please wait.")

        for i in range(10):
            time.sleep(.3)
            print(".", end='', flush=True)

            result = self.calculate_attack_result()

            if result == 0:
                print("\nRESULT: No winner")

            if result == 1:
                print("\nRESULT: You hit your opponent")
                self.hit_opponent(opponent)

            if result == 2:
                print("\nRESULT: You got hit by your opponent")
                self.hit_opponent(self)

    def calculate_attack_result(self):
        return random.randint(0, 2)

    def escape(self):
        print("Escaping...")
        for i in range(10):
            time.sleep(.3)
            print("\n", flush=True)
        print("Your opponent caught you")

    def hit_opponent(self, opponent):
        opponent.hit += 1
        opponent.energy -= 1
        if opponent.hit % 5 == 0:
            opponent.health -= 1

        if opponent.health < 1:
            opponent.energy = 0

            print("{} won the game!".format(self.name))
            self.exit_game()

    def exit_game(self):
        print("Exiting...")
        sys.exit()


you = Player("Burak")
opponent = Player("Paul")

while True:
    print("You are facing your opponent right now.", "Your move:", "Attack: a", "Escape: e", "Exit: q", sep="\n")

    move = input("\n>")

    if move == 'a':

        you.attack(opponent)

        print("Opponent's State")
        opponent.display_current_state()

        print("Your State")
        you.display_current_state()

    if move == 'e':
        you.escape()

    if move == 'q':
        you.exit_game()
