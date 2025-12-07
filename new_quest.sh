#!/bin/zsh

YEAR_DIR="$(dirname "$0")/2024"
LAST_QUEST=$(ls -d "$YEAR_DIR"/quest_* 2>/dev/null | sort -V | tail -1 | grep -oE '[0-9]+$')

if [ -z "$LAST_QUEST" ]; then
    NEXT_QUEST=1
else
    NEXT_QUEST=$((10#$LAST_QUEST + 1))
fi

NEXT_QUEST_FORMATTED=$(printf "%02d" $NEXT_QUEST)
QUEST_DIR="$YEAR_DIR/quest_$NEXT_QUEST_FORMATTED"

mkdir -p "$QUEST_DIR"

cat > "$QUEST_DIR/main.py" << 'EOF'
def part_1(notes):
    pass


def part_2(notes):
    pass


def part_3(notes):
    pass


def get_data(file_path):
    with open(file_path, "r") as file:
        notes = [row.strip() for row in file]
    return notes


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    notes = get_data(PATH / "notes1.txt")
    part_1(notes)

    notes = get_data(PATH / "notes2.txt")
    part_2(notes)

    notes = get_data(PATH / "notes3.txt")
    part_3(notes)
EOF

# Create empty notes files
touch "$QUEST_DIR/notes1.txt"
touch "$QUEST_DIR/notes2.txt"
touch "$QUEST_DIR/notes3.txt"

echo "Created quest_$NEXT_QUEST_FORMATTED in $YEAR_DIR"
