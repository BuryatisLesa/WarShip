from random import randint, choice


# class Board:
#     def __init__(self):
#         self.size = 6
#
#     def add_ship(self):
#         busy = []
#         ship = []
#         one_lvl = 0
#         while one_lvl < 4:
#             x = randint(0, self.size)
#             y = randint(0, self.size)
#             random_ship = (y, x)
#             near = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1), (y, x)]
#             valid_b = []
#             for valid_busy in busy:
#                 a = valid_busy == random_ship
#                 valid_b.append(a)
#             if not any(valid_b):
#                 for i in near:
#                     busy.append(i)
#                 one_lvl += 1
#                 ship.append(random_ship)
#         two_lvl = 0
#         while two_lvl < 2:
#             x = randint(0, self.size)
#             y = randint(0, self.size)
#             orien = choice((0,1))
#             if orien == 1:
#                 random_ship = (y, x)
#                 near = [(y - 2, x),(y, x - 1),(y, x + 1),(y - 1, x + 1),(y - 1, x - 1), (y, x)]
#                 valid_b = []
#                 for valid_busy in busy:
#                     a = valid_busy == random_ship
#                     valid_b.append(a)
#                 if not any(valid_b):
#                     for i in near:
#                         busy.append(i)
#                     ship.append(random_ship)
#                     ship.append((y - 1, x))
#                     two_lvl += 1
#             if orien == 0:
#                 random_ship = (y, x)
#                 near = [(y - 1, x),(y + 1, x),(y, x - 1),(y, x - 2),(y - 1, x + 1), (y + 1, x + 1), (y,x), (y, x + 1)]
#                 valid_b = []
#                 for valid_busy in busy:
#                     a = valid_busy == random_ship
#                     valid_b.append(a)
#                 if not any(valid_b):
#                     for i in near:
#                         busy.append(i)
#                     ship.append(random_ship)
#                     ship.append((y, x + 1))
#                     two_lvl += 1
#         return ship
#
# board = Board()
# print(len(board.add_ship()))


class Player:
    """Класс, который отвечает, за взаимодействие игрока"""
    def __init__(self):
        self.step_coords = [(2,2),(1,2)]

    def step_player(self):
        loop = True
        while loop:
            self.valid = []
            x = int(input('Введите координату X: '))
            y = int(input('Введите координату Y: '))
            v_coords = (y,x)
            for i in self.step_coords:
                a = i == v_coords
                self.valid.append(a)
            if not any(self.valid):
                coords = (y,x)
                self.step_coords.append((y, x))
                loop = False
                return coords
            else:
                print('Некорректно введены данные!')


player = Player()
player.step_player()
print(player.step_coords)
