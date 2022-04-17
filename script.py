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


class Game:
    turn = 1

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


def print_divider():
    print("-" * 60)


def introduce_players():
    print(
        f"{player_one.color} {player_one.name} {reset_color} and {player_two.color} {player_two.name} {reset_color} are playing the game"
    )


print_divider()

game = Game()

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

print_circles()


game_is_running = True


def select_circle():
    player = None
    if Game.turn == 1:
        player = player_one

    elif Game.turn == 2:
        player = player_two

    circle = input(
        f"{player.color} {player.name} {reset_color}, select a circle (enter letter and number): "
    )

    while True:
        try:
            if (
                not type(circle[0]) is str or not circle[1].isnumeric()
            ):  # check if the input is valid
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid circle(enter letter and number)")
            circle = input(
                f"{player.color} {player.name} {reset_color}, select a circle (enter letter and number): "
            )

    circle_letter = circle[0].upper()
    circle_number = int(circle[1])

    for circle in circles:
        if circle.letter == circle_letter and circle.number == circle_number:
            result = player.add_circle(circle)
            if result:
                Game.turn = 2 if Game.turn == 1 else 1
                print_circles()


while game_is_running:
    select_circle()

    # while True:
    #     print("Select a circle: ")
    #     circle_to_select = input("Enter a circle: ")
    #     if circle_to_select.isalpha() and circle_to_select.upper() in letters_list:
    #         circle_to_select = circle_to_select.upper()
    #         for circle in circles:
    #             if circle.letter == circle_to_select:
    #                 return circle
    #     else:
    #         print("Please enter a valid circle")
    #         continue

print_divider()


print_divider()


print(yellow_color + "Warning!" + reset_color)
print(red_color + "Failure!" + reset_color)
print(green_color + "Success!" + reset_color)
print(blue_color + "Information!" + reset_color)
