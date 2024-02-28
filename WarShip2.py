from random import randint, choice


class Dot:
    """Класс, который отвечает за отметкой ходов в случае промаха"""
    def __init__(self, board, ship):
        self.__board = board
        self.__ship = ship
        self.__coords = []

    @property
    def board(self):
        return self.__board

    @property
    def coords(self):
        return self.__coords

    @property
    def ship(self):
        return self.__ship

    def shot_dot(self, coords):
        self.__coords.append(coords)
        valid = []
        for _ in self.ship:
            move = _ == coords
            valid.append(move)
        if any(valid):
            return True
        else:
            return False

    def move(self, valid, player):
        if not valid:
            for y, x in self.coords:
                self.board[y][x] = 'T'
            print(f'{player} - мимо')
            return self.board
        if valid:
            for y, x in self.coords:
                self.board[y][x] = 'X'
            print(f'{player} - попал!')
            return self.board

#######################################################


class Ship:
    """Класс, который отвечает за взаимодействие кораблей"""
    def __init__(self):
        self.__lvl_ship = [1,1,1,1,2,2,3]
        self.__orien = [0, 1]

    @property
    def lvl_ship(self):
        return self.__lvl_ship

    @lvl_ship.setter
    def lvl_ship(self, list):
        self.__lvl_ship = list

    @property
    def orien(self):
        return self.__orien

    @orien.setter
    def orien(self, other):
        self.__orien = other

########################################################


class Board:
    """Класс, который отвечает, за объекты на доске"""
    def __init__(self):
        self.__size = 6
        self.__board = [['0'] * (self.__size + 1) for i in range(self.__size + 1)]
        self.ship = []
        self.busy = []

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, other_board):
        self.__board = other_board

    @property
    def get_ship(self):
        return self.ship

    @property
    def get_busy(self):
        return self.busy

    def print_ai(self, board):
        board[0] = [i for i in range(self.__size + 1)]
        for j in range(7):
            board[j][0] = j
        for i in board:
            save = str(i).replace(",", ' |')
            save_1 = save.replace("■", "'0'")
            save_2 = save_1.replace("'", '')
            print(save_2)

    def print_user(self, board):
        board[0] = [i for i in range(self.__size + 1)]
        for j in range(7):
            board[j][0] = j
        for i in board:
            save = str(i).replace(",", ' |')
            save_2 = save.replace("'", '')
            print(save_2)

    def add_ship(self):
        three_lvl = 0
        while three_lvl < 1:
            orien = choice((0, 1))
            if orien == 1:
                x = randint(1, self.size)
                y = randint(3, self.size)
                near = [(y - 3, x), (y, x - 1), (y, x + 1), (y - 1, x + 1), (y - 1, x - 1), (y - 2, x - 1),
                        (y - 2, x + 1), (y, x), (y - 2, x), (y - 1, x), (y + 1, x)]
                random_ship = (y, x)
                random_ship_two = (y - 2, x)
                random_ship_three = (y - 1, x)
                valid_b = []
                valid_b_two = []
                valid_b_three = []
                for valid_busy in self.busy:
                    a = valid_busy == random_ship
                    valid_b.append(a)
                for valid_busy_two in self.busy:
                    a = valid_busy_two == random_ship_two
                    valid_b_two.append(a)
                for valid_busy_three in self.busy:
                    a = valid_busy_three == random_ship_three
                    valid_b_two.append(a)
                if not any(valid_b) and not any(valid_b_two) and not any(valid_b_three):
                    for i in near:
                        self.busy.append(i)
                    self.ship.append(random_ship)
                    self.ship.append((y - 2, x))
                    self.ship.append((y - 1, x))
                    three_lvl += 1
            if orien == 0:
                x = randint(1, self.size - 2)
                y = randint(1, self.size)

                near = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 3), (y - 1, x + 1), (y + 1, x + 1), (y - 1, x + 2),
                        (y + 1, x + 2), (y, x), (y, x + 1), (y, x + 2)]
                random_ship = (y, x)
                random_ship_two = (y, x + 1)
                random_ship_three = (y, x + 2)
                valid_b = []
                valid_b_two = []
                valid_b_three = []
                for valid_busy in self.busy:
                    a = valid_busy == random_ship
                    valid_b.append(a)
                for valid_busy_two in self.busy:
                    a = valid_busy_two == random_ship_two
                    valid_b_two.append(a)
                for valid_busy_three in self.busy:
                    a = valid_busy_three == random_ship_three
                    valid_b_two.append(a)
                if not any(valid_b) and not any(valid_b_two) and not any(valid_b_three):
                    for i in near:
                        self.busy.append(i)
                    self.ship.append(random_ship)
                    self.ship.append((y, x + 1))
                    self.ship.append((y, x + 2))
                    three_lvl += 1
        two_lvl = 0
        while two_lvl < 2:
            #  0 == горизонтальная ориентация
            #  1 == вертикальная ориентация
            orien = choice((0, 1))
            if orien == 1:
                x = randint(1, self.size)
                y = randint(2, self.size)
                random_ship = (y, x)
                near = [(y - 2, x), (y, x - 1), (y, x + 1), (y - 1, x + 1), (y - 1, x - 1), (y, x), (y + 1, x)]
                valid_b = []
                random_ship_two = (y - 1, x)
                for valid_busy in self.busy:
                    a = valid_busy == random_ship
                    valid_b.append(a)
                valid_b_two = []
                for valid_busy_two in self.busy:
                    a = valid_busy_two == random_ship_two
                    valid_b_two.append(a)
                if not any(valid_b) and not any(valid_b_two):
                    for i in near:
                        self.busy.append(i)
                    self.ship.append(random_ship)
                    self.ship.append((y - 1, x))
                    two_lvl += 1
            if orien == 0:
                x = randint(1, self.size - 1)
                y = randint(1, self.size)
                random_ship = (y, x)
                near = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 2), (y - 1, x + 1), (y + 1, x + 1), (y, x),
                        (y, x + 1), (y, x - 1)]
                valid_b = []
                random_ship_two = (y, x + 1)
                for valid_busy in self.busy:
                    a = valid_busy == random_ship
                    valid_b.append(a)
                valid_b_two = []
                for valid_busy_two in self.busy:
                    a = valid_busy_two == random_ship_two
                    valid_b_two.append(a)
                if not any(valid_b) and not any(valid_b_two):
                    for i in near:
                        self.busy.append(i)
                    self.ship.append(random_ship)
                    self.ship.append((y, x + 1))
                    two_lvl += 1
        one_lvl = 0
        while one_lvl < 4:
            x = randint(1, self.size)
            y = randint(1, self.size)
            random_ship = (y, x)
            near = [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1), (y ,x)]
            valid_b = []
            for valid_busy in self.busy:
                a = valid_busy == random_ship
                valid_b.append(a)
            if not any(valid_b):
                for i in near:
                    self.busy.append(i)
                self.ship.append(random_ship)
                one_lvl += 1

#########################################################


class Player:
    """Класс, который отвечает, за взаимодействие игрока"""
    def __init__(self):
        self.board = Board()
        self.board.add_ship()
        self.ship = self.board.ship
        self.busy = self.board.busy
        self.coords_player = []

    def step_player(self):
        loop = True
        while loop:
            try:
                self.valid = []
                x = int(input('Введите координату X: '))
                y = int(input('Введите координату Y: '))
            except ValueError:
                print('Ввести можно только целочисленные значения (1,2,3 и т.д)')
            except IndexError:
                print('Ядро вылетело за границы поля!')
            else:
                v_coords = (y,x)
                for i in self.coords_player:
                    a = i == v_coords
                    self.valid.append(a)
                if 1 <= x <= self.board.size and 1 <= y <= self.board.size and not any(self.valid):
                    coords = (y,x)
                    self.coords_player.append((y, x))
                    loop = False
                    return coords
                if any(self.valid):
                    print('Вы попали в тоже место, попытайтесь снова!')
                else:
                    print('Некорректно введены данные!')

    def board_player(self):
        for y, x in self.ship:
            self.board.board[y][x] = '■'
        return self.board.board

    def print_board(self):
        self.board.print_user(self.board.board)



#########################################################
class User(Player):
    def __str__(self):
        return 'Игровое поле игрока:'


#########################################################
class AI(Player):
    """Класс, который отвечает, за ходы компьютера"""
    def __init__(self):
        super().__init__()
        self.coords_ai =[]

    def __str__(self):
        return 'Игровое поле компьютера:'

    def step_player(self):
        loop = True
        while loop:
            self.valid = []
            x = randint(1,6)
            y = randint(1,6)
            for i in self.coords_player:
                a = i == (y,x)
                self.valid.append(a)
            if not any(self.valid):
                coords = (y,x)
                self.coords_player.append((y,x))
                print(f'Компьютер сходил {y},{x}')
                return coords
    def print_board(self):
        self.board.print_ai(self.board.board)
#########################################################


class Game:
    """Класс, который отвечает, за ходом игры"""
    def start_game(self):
        print('\033[35m-------------------------\n'
              'Welcome in game "WarShip"'
              '\n-------------------------\033[31m\n\033[40m'
              '----------------------------------------\n'
              'Вам даётся 1 корабль на 3 ячейки - ■ ■ ■\n'
              '2 корабля на 2 ячейки - ■ ■ \n'
              '4 корабля на 1 ячейку - ■\n'
              '----------------------------------------\033[0m')
        board = Board()
        ai = AI()
        user = User()
        print(ai)
        ai_board = ai.board_player()
        user_board = user.board_player()
        ai.print_board()
        self.split_game()
        print(user)
        user.print_board()
        loop = True
        while loop:
            step_user = user.step_player()
            step_ai = ai.step_player()
            dot_user = Dot(ai_board, ai.ship)
            dot_ai = Dot(user_board, user.ship)
            try:
                dot_ai.move(dot_ai.shot_dot(step_ai), 'Компьютер')
                dot_user.move(dot_user.shot_dot(step_user),'Игрок')
            except IndexError:
                print('Минимальное значение координат от 1 до 6!')
                raise('НАЧНИТЕ ЗАНОВО!')
            except TypeError:
                print('Минимальное значение координат от 1 до 6!')
                raise('НАЧНИТЕ ЗАНОВО!')
            self.end_game(ai.ship,step_user,'Игрок')
            self.end_game(user.ship,step_ai,'Компьютер')
            print(ai)
            board.print_ai(dot_user.board)
            self.split_game()
            print(user)
            board.print_user(dot_ai.board)

    def split_game(self):
        print('-' * 27)

    def end_game(self, ship, coords, name_player):
        valid = []
        player = ship
        for _ in player:
            v = _ == coords
            valid.append(v)
        if any(valid):
            player.remove(coords)
        if player == []:
            print(f'Победил {name_player}')
            raise('КОНЕЦ ИГРЫ!')

##########################################################
if __name__ == '__main__':
    game = Game()
    game.start_game()


