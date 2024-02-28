import random
from random import randint


#
#
# if __name__ == '__main__':
#     # size = 6
#     # a = [['0' for i in range(size)] for j in range(size)]
#     # x = -1
#     # y = 0
#     # a[y][x] = '#'
#     # busy = []
#     # ship = []
#     # if a[y][x] == '#':
#     #     busy.append((y - 1, x))
#     #     busy.append((y + 1, x))
#     #     busy.append((y, x - 1))
#     #     busy.append((y, x + 1))
#     #     ship.append((y, x))
#     # print(busy)
#     # print(ship)
#     # for i, j in busy:
#     #     print(i, j)
#     #
#     # for i in a:
#     #     print(i)
#     a = [(2 - 1, 5 - 3)]
#     for i, j in a:
#         print(i, j)

class Board:
    def __init__(self):
        self.busy = []
        self.ship = list(set([]))
        self.size = 6

    def add_ship(self):
        one_lvl = 0
        while one_lvl < 4:
            x = randint(0, self.size)
            y = randint(0, self.size)
            random_ship = (y, x)
            near = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]
            valid_s = []
            for valid_ship in self.ship:
                a = valid_ship == random_ship
                valid_s.append(a)
            if not any(valid_s):
                valid_b = []
                for valid_busy in self.busy:
                    b = valid_busy == random_ship
                    valid_b.append(b)
                if not any(valid_b):
                    for i in near:
                        self.busy.append(i)
                    one_lvl += 1
                    self.ship.append(random_ship)
        two_lvl = 0
        while two_lvl < 2:
            x = randint(0, self.size)
            y = randint(0, self.size)
            orien = random.choice((0,1))
            if orien == 1:
                random_ship = (y, x)
                near = [(y - 2, x),(y, x - 1),(y, x + 1),(y - 1, x + 1),(y - 1, x - 1), (y, x)]
                valid_two = []
                for valid_ship in self.ship:
                    a = valid_ship == random_ship
                    valid_two.append(a)
                if not any(valid_two):
                    valid_b_two = []
                    for valid_busy in self.busy:
                        b = valid_busy == random_ship
                        valid_b_two.append(b)
                    if not any(valid_b_two):
                        for i in near:
                            self.busy.append(i)
                        two_lvl += 1
                        self.ship.append(random_ship)
                        self.ship.append((y - 1, x))
            if orien == 0:
                random_ship = (y, x)
                near = [(y - 1, x),(y + 1, x),(y, x - 1),(y, x - 2),(y - 1, x + 1), (y + 1, x + 1), (y,x), (y, x + 1)]
                valid_s = []
                for valid_ship in self.ship:
                    a = valid_ship == random_ship
                    valid_s.append(a)
                if not any(valid_s):
                    valid_b = []
                    for valid_busy in self.busy:
                        b = valid_busy == random_ship
                        valid_b.append(b)
                    if not any(valid_b):
                        for i in near:
                            self.busy.append(i)
                        two_lvl += 1
                        self.ship.append(random_ship)
                        self.ship.append((y, x + 1))
        # three_lvl = 0
        # while three_lvl < 1:
        #     x = randint(0, self.size)
        #     y = randint(0, self.size)
        #     orien = random.choice((0, 1))
        #     if orien == 1:
        #         random_ship = (y, x)
        #         near = [(y - 3, x), (y, x - 1), (y, x + 1), (y - 1, x + 1), (y - 1, x - 1), (y - 2, x - 1),
        #                 (y - 2, x + 1), (y, x), (y - 2, x), (y - 1, x)]
        #         valid_s = []
        #         for valid_ship in self.ship:
        #             a = valid_ship == random_ship
        #             valid_s.append(a)
        #         if not any(valid_s):
        #             valid_b = []
        #             for valid_busy in self.busy:
        #                 b = valid_busy == random_ship
        #                 valid_b.append(b)
        #             if not any(valid_b):
        #                 for i in near:
        #                     self.busy.append(i)
        #                 three_lvl += 1
        #                 self.ship.append(random_ship)
        #                 self.ship.append((y - 2, x))
        #                 self.ship.append((y - 1, x))
        #     if orien == 0:
        #         random_ship = (y, x)
        #         near = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x - 3), (y - 1, x + 1), (y + 1, x + 1), (y - 1, x - 2),
        #                 (y + 1, x - 2), (y, x), (y, x + 1), (y, x + 2)]
        #         valid_s = []
        #         for valid_ship in self.ship:
        #             a = valid_ship == random_ship
        #             valid_s.append(a)
        #         if not any(valid_s):
        #             valid_b = []
        #             for valid_busy in self.busy:
        #                 b = valid_busy == random_ship
        #                 valid_b.append(b)
        #             if not any(valid_b):
        #                 for i in near:
        #                     self.busy.append(i)
        #                 three_lvl += 1
        #                 self.ship.append(random_ship)
        #                 self.ship.append((y, x + 1))
        #                 self.ship.append((y, x + 2))


board = Board()
board.add_ship()
print(len(board.ship))
print(board.busy)



