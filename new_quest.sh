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


if __name__ == "__main__":
    from pathlib import Path

    PATH = Path(__file__).parent

    with open(PATH / "notes.txt", "r") as file:
        notes = [row.strip() for row in file]

        part_1(notes)
        part_2(notes)
        part_3(notes)
EOF

# Create empty notes.txt
touch "$QUEST_DIR/notes.txt"

echo "Created quest_$NEXT_QUEST_FORMATTED in $YEAR_DIR"
