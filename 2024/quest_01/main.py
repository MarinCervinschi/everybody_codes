potions = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}


def part_1(notes):
    from collections import Counter

    print(sum([potions[k] * v for k, v in Counter(notes).items()]))


def part_2_3(notes, size, part3=False):
    ans = 0
    for i in range(0, len(notes), size):
        pair = [notes[i + j] for j in range(size)]

        x = pair.count("x")
        sup = 0
        if part3:
            if x == 1:
                sup = 2
            elif x == 0:
                sup = 6
        elif x == 0:
            sup = 2

        ans += sum([potions[c] for c in pair]) + sup

    print(ans)


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    with open(PATH / "notes.txt", "r") as file:
        notes = [row.strip() for row in file]

        part_1(notes[0])
        part_2_3(notes[1], size=2)
        part_2_3(notes[2], size=3, part3=True)
