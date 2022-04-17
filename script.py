import random

green_color = "\x1b[6;30;42m"
red_color = "\x1b[6;30;41m"
yellow_color = "\x1b[6;30;43m"
blue_color = "\x1b[6;30;44m"
reset_color = "\x1b[0m"  # reset color


def create_dict():
    ran_letter_idx = random.randint(0, 6)
    ran_number_idx = random.randint(0, 5)
    dict = {}
    letters_list = ["a", "b", "c", "d", "e", "f", "g"]
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


def fill_in_circles():
    for row in range(1, 7):  # for each row
        for col in range(1, 8):  # for each column
            letters_list = ["a", "b", "c", "d", "e", "f", "g"]
            letter = letters_list[col - 1]
            number = row
            circle = Circle(letter, number, row, col)  # create circle
            circles.append(circle)


circles = []
fill_in_circles()


print(yellow_color + "Warning!" + reset_color)
print(red_color + "Failure!" + reset_color)
print(green_color + "Success!" + reset_color)
print(blue_color + "Information!" + reset_color)
