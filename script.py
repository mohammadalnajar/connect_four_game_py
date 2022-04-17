import random

green_color = "\x1b[6;30;42m"
red_color = "\x1b[6;37;41m"
yellow_color = "\x1b[6;30;43m"
blue_color = "\x1b[1;37;44m"
reset_color = "\x1b[0m"  # reset color
letters_list = ["A", "B", "C", "D", "E", "F", "G"]


def create_dict():
    ran_letter_idx = random.randint(0, 6)
    ran_number_idx = random.randint(0, 5)
    dict = {}
    letters_list = ["A", "B", "C", "D", "E", "F", "G"]
    numbers_list = [1, 2, 3, 4, 5, 6]
    dict[letters_list[ran_letter_idx]] = numbers_list[ran_number_idx]
    return dict


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
            print(f"This circle is already owned by{self.owner}")
            return False  # failed to set owner


class Player:
    count = 1  # count of players

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

        color = input(
            f"Enter a color for player {Player.count} ('g' for green / 'r' for red ): "
        )
        # check if the color is valid
        while True:
            try:
                if color.isnumeric() or color.lower() not in ["g", "r", "red", "green"]:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid color(only 'g' or 'r' is allowed)")
                color = input(
                    f"Enter a color for player {Player.count} ('g' for green / 'r' for red ): "
                )
        self.color = green_color if color == "g" or color == "green" else red_color

        self.color_name = "green" if color == "g" or color == "green" else "red"

        self.circles = []

        Player.count += 1

    def __repr__(self) -> str:
        return f"The player {self.name} has the color {self.color} {self.color_name} {reset_color}"


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


print("=" * 60)
print_circles()
print("=" * 60)

player_one = Player()

print(player_one)

print(yellow_color + "Warning!" + reset_color)
print(red_color + "Failure!" + reset_color)
print(green_color + "Success!" + reset_color)
print(blue_color + "Information!" + reset_color)
