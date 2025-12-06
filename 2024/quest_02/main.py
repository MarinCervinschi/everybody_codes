import re


def part_1(texts, words):
    print(sum(texts.count(w) for w in words))


def part_2(texts, words):

    ans = 0
    for text in texts:
        for word in text.split(" "):
            ans += len(get_matched_positions(word, words))

    print(ans)


def get_matched_positions(text, words):
    matched_positions = set()
    for w in words:
        for match in re.finditer(rf"(?=({w}|{w[::-1]}))", text):
            start = match.start()
            matched_positions.update(range(start, start + len(w)))

    return matched_positions


def part_3(texts, words):
    ans = 0

    visited = [[0] * len(texts[0]) for _ in range(len(texts))]

    for row, text in enumerate(texts):
        matched_positions = get_matched_positions(text, words)
        pos = get_matched_positions(text + text, words)
        matched_positions.update(pos)
        ans += len(matched_positions)
        for col in matched_positions:
            if visited[row][col % len(text)] == 0:
                visited[row][col % len(text)] = 1
            else:
                ans -= 1

    import numpy as np

    temp = [list(t) for t in texts]
    texts = np.transpose(temp).tolist()
    for col, text in enumerate(texts):
        matched_positions = get_matched_positions("".join(text), words)
        ans += len(matched_positions)
        for row in matched_positions:
            if visited[row][col] == 0:
                visited[row][col] = 1
            else:
                ans -= 1

    print(ans)


def get_data(file_path):
    with open(file_path, "r") as file:
        notes = [row.strip() for row in file]
        words = notes[0].split(":")[1].split(",")
        texts = notes[2:]
    return words, texts


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    words, texts = get_data(PATH / "notes1.txt")
    part_1(texts[0], words)

    words, texts = get_data(PATH / "notes2.txt")
    part_2(texts, words)

    words, texts = get_data(PATH / "notes3.txt")
    part_3(texts, words)
