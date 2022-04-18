import random

green_color = "\x1b[6;30;42m"  # green color
red_color = "\x1b[6;37;41m"  # red color
yellow_color = "\x1b[6;30;43m"  # yellow color
blue_color = "\x1b[1;37;44m"  # blue color
reset_color = "\x1b[0m"  # reset color
letters_list = ["A", "B", "C", "D", "E", "F", "G"]  # list of letters for columns


def create_dict():
    ran_letter_idx = random.randint(0, 6)
    ran_number_idx = random.randint(0, 5)
    dict = {}
    letters_list = ["A", "B", "C", "D", "E", "F", "G"]
    numbers_list = [1, 2, 3, 4, 5, 6]
    dict[letters_list[ran_letter_idx]] = numbers_list[ran_number_idx]
    return dict


def print_divider():
    print("-" * 60)


def clear_screen():
    print(chr(27) + "[2j")
    print("\033c")
    print("\x1bc")


clear_screen()


class Game:
    turn = 1
    game_is_running = True
    won_player = None

    def __init__(self):
        self.winner = None


class Circle:
    def __init__(self, letter, number, row, col) -> None:
        self.letter = letter  # letter
        self.number = number  # number
        self.row = row
        self.col = col
        self.owner = None  # owner of the circle
        self.color = blue_color  # color of the circle

    def __repr__(self) -> str:
        return f"{self.letter}{self.number}"

    def set_owner(self, player):
        if self.owner is None:  # if the circle is not owned
            self.owner = player  # set owner
            self.color = player.color  # set color

            return True  # successfully set owner
        else:
            print(
                f"This circle is already owned by {self.color} {self.owner.name} {reset_color}"
            )

            return False  # failed to set owner


class Player:
    count = 1  # count of players
    taken_colors = []

    def __init__(self) -> None:
        name = input(f"Enter a name for player {Player.count}: ")

        # check if the name is valid
        while True:
            try:
                if not type(name) is str or name.isnumeric():
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid name(only text is allowed)")
                name = input(f"Enter a name for player {Player.count}: ")

        self.name = name
        color = ""
        if len(Player.taken_colors) > 0:
            if "red" in Player.taken_colors or "r" in Player.taken_colors:
                color = "green"
            else:
                color = "red"
        else:
            color = input(
                f"Enter a color for player {Player.count} ('g' for green / 'r' for red ): "
            )
            # check if the color is valid
            while True:
                try:
                    if color.isnumeric() or color.lower() not in [
                        "g",
                        "r",
                        "red",
                        "green",
                    ]:
                        raise ValueError
                    break
                except ValueError:
                    print("Please enter a valid color(only 'g' or 'r' is allowed)")
                    color = input(
                        f"Enter a color for player {Player.count} ('g' for green / 'r' for red ): "
                    )
        self.color = green_color if color == "g" or color == "green" else red_color

        self.color_name = "green" if color == "g" or color == "green" else "red"
        Player.taken_colors.append(self.color_name)
        self.circles = []

        Player.count += 1

    def __repr__(self) -> str:
        return f"The player {self.name} has the color {self.color} {self.color_name} {reset_color}"

    def add_circle(self, circle):
        if circle.set_owner(self):
            self.circles.append(circle)
            return True
        else:
            return False


def fill_in_circles():
    for row in range(1, 7):  # for each row
        for col in range(1, 8):  # for each column
            letter = letters_list[col - 1]
            number = row
            circle = Circle(letter, number, row, col)  # create circle
            circles.append(circle)


circles = []

fill_in_circles()


def print_circles():
    for row in range(0, 7):
        str_to_print = ""
        if row == 0:
            for letter in letters_list:
                if not letter == "A":
                    str_to_print += " <-> "
                str_to_print += f"{yellow_color} {letter.upper()}  {reset_color}"
        else:
            idx = 0
            for circle in circles:
                if circle.row == row:
                    if not idx % 7 == 0:
                        str_to_print += " <-> "
                    circle_to_print = f"{circle.color} {circle} {reset_color}"
                    str_to_print += circle_to_print
                idx += 1
        print(str_to_print)
        print("-" * 60)


def introduce_players():
    print(
        f"{player_one.color} {player_one.name} {reset_color} and {player_two.color} {player_two.name} {reset_color} are playing the game"
    )


print_divider()

Game()

players = []

player_one = Player()
players.append(player_one)
print(player_one)

print_divider()

player_two = Player()
players.append(player_two)
print(player_two)

print_divider()

introduce_players()

print_divider()
print_divider()
print_divider()

print_circles()


def select_circle():
    player = player_one if Game.turn == 1 else player_two

    letter = input(
        f"{player.color} {player.name} {reset_color}, select a circle (enter letter): "
    )

    while True:  # check if column is full
        try:
            while True:  # check if the input is valid
                try:
                    if not type(letter) is str:
                        raise ValueError
                    break
                except ValueError:  # if the input is not valid
                    print("Please enter a valid circle(enter a letter)")
                    letter = input(
                        f"{player.color} {player.name} {reset_color}, select a circle (enter a letter): "
                    )

            error = {}

            circle_letter = letter.upper()

            # check if the input is a number
            if circle_letter.isnumeric():
                error["msg"] = "******* Only letters are allowed *******"
                raise ValueError

            # check if the letter is valid
            if circle_letter not in letters_list:
                error["msg"] = "******* The selected letter is not valid *******"
                raise ValueError

            # get the circles in the column
            col_circles = []
            for circle in circles:
                if circle.letter == circle_letter and circle.owner is None:
                    col_circles.append(circle)

            # check if the column is full
            if len(col_circles) == 0:
                error["msg"] = "******* The selected column is full *******"
                raise ValueError
            else:
                added = player.add_circle(
                    col_circles[-1]
                )  # add the circle to the player
                if added:
                    Game.turn = 2 if Game.turn == 1 else 1  # change turn
                break
        except ValueError:  # if the column is full
            msg = error["msg"] if "msg" in error else "invalid input"
            print(f"{msg}")
            letter = input(
                f"{player.color} {player.name} {reset_color}, select a circle (enter letter): "
            )


def check_for_win():

    if Game.won_player:  # if the game is already won
        Game.game_is_running = False
        print(
            f"{Game.won_player.color} {Game.won_player.name} {reset_color} won the game"
        )


while Game.game_is_running:
    select_circle()
    clear_screen()
    print_circles()
    check_for_win()

# restart the game
# def restart_game():


print_divider()


print_divider()


print(yellow_color + "Warning!" + reset_color)
print(red_color + "Failure!" + reset_color)
print(green_color + "Success!" + reset_color)
print(blue_color + "Information!" + reset_color)
