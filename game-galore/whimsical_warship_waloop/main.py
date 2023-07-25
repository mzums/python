import random
from itertools import product


class Game:

    def __init__(self, board_size):
        self.board_size = board_size

    def place_ships(self, number_of_ships):
        self.board = [["-"] * board_size for _ in range(board_size)]
        #self.xy = [(random.choice(range(board_size)), random.choice(range(board_size))) for _ in range(number_of_ships)]
        #self.xy = random.sample([(x, y) for x in range(board_size) for y in range(board_size)], number_of_ships)
        self.xy = random.sample(list(product(range(board_size), repeat=2)), number_of_ships)

    def players_turn(self):
        print(f"{len(self.xy)} ships remaining!")
        print("\n".join(["  ".join(row) for row in self.board]))

        x = int(input(f"Pick row 0-{self.board_size}: "))
        y = int(input(f"Pick column 0-{self.board_size}: "))
        if (x, y) in self.xy:
            print("Hit and sunk!")
            self.xy.remove((x, y))
            self.board[x][y] = 'X'
        else:
            print("Mishit!")

    def start(self):
        self.place_ships(4)
        while(len(self.xy)):
            self.players_turn()
        print("You won!!!")


if __name__ == "__main__":
    print("Welcome to Whimsical Warship waloop!")
    board_size = int(input("Enter size of your battle field: "))
    print("Good luck!")
    game = Game(board_size)
    game.start()