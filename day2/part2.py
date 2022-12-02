"""
--- Part Two ---

The Elf finishes helping with the tent and sneaks back over to you.
"Anyway, the second column says how the round needs to end: X means you
need to lose, Y means you need to end the round in a draw, and Z means
you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to
figure out what shape to choose so the round ends as indicated. The
example above now goes like this:

- In the first round, your opponent will choose Rock (A), and you need
  the round to end in a draw (Y), so you also choose Rock. This gives
  you a score of 1 + 3 = 4.
- In the second round, your opponent will choose Paper (B), and you
  choose Rock so you lose (X) with a score of 1 + 0 = 1.
- In the third round, you will defeat your opponent's Scissors with
  Rock for a score of 1 + 6 = 7.

Now that you're correctly decrypting the ultra top secret strategy
guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your
total score be if everything goes exactly according to your strategy
guide?
"""

OPPONENT_ROCK = "A"
OPPONENT_PAPER = "B"
OPPONENT_SCISSORS = "C"

LOSS = 0
DRAW = 1
WIN = 2

YOU_ROCK = "X"
YOU_PAPER = "Y"
YOU_SCISSORS = "Z"

POINTS = {
    YOU_ROCK: 1,
    YOU_PAPER: 2,
    YOU_SCISSORS: 3
}

LOSS_POINTS = 0
DRAW_POINTS = 3
WIN_POINTS = 6

RESULTS = {
    f"{OPPONENT_ROCK}{YOU_ROCK}": DRAW,
    f"{OPPONENT_ROCK}{YOU_PAPER}": WIN,
    f"{OPPONENT_ROCK}{YOU_SCISSORS}": LOSS,
    f"{OPPONENT_PAPER}{YOU_ROCK}": LOSS,
    f"{OPPONENT_PAPER}{YOU_PAPER}": DRAW,
    f"{OPPONENT_PAPER}{YOU_SCISSORS}": WIN,
    f"{OPPONENT_SCISSORS}{YOU_ROCK}": WIN,
    f"{OPPONENT_SCISSORS}{YOU_PAPER}": LOSS,
    f"{OPPONENT_SCISSORS}{YOU_SCISSORS}": DRAW,
}

REQUIRED_ACTIONS = {
    "X": LOSS,
    "Y": DRAW,
    "Z": WIN,
}

DESIRED_RESULTS = {
    f"{OPPONENT_ROCK}X": YOU_SCISSORS,
    f"{OPPONENT_ROCK}Y": YOU_ROCK,
    f"{OPPONENT_ROCK}Z": YOU_PAPER,
    f"{OPPONENT_PAPER}X": YOU_ROCK,
    f"{OPPONENT_PAPER}Y": YOU_PAPER,
    f"{OPPONENT_PAPER}Z": YOU_SCISSORS,
    f"{OPPONENT_SCISSORS}X": YOU_PAPER,
    f"{OPPONENT_SCISSORS}Y": YOU_SCISSORS,
    f"{OPPONENT_SCISSORS}Z": YOU_ROCK,
}


def main():
    points = 0

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            opponent, desired_result = line.strip().split()
            result = REQUIRED_ACTIONS[desired_result]
            if result == DRAW:
                points += DRAW_POINTS
            elif result == WIN:
                points += WIN_POINTS

            my_action = DESIRED_RESULTS[f"{opponent}{desired_result}"]
            points += POINTS[my_action]

    print(f"Using the complete strategy guide, my score will be {points}")


if __name__ == "__main__":
    main()
