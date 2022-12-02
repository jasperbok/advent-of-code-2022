"""
--- Day 2: Rock Paper Scissors ---

The Elves begin to set up camp on the beach. To decide whose tent gets
to be closest to the snack storage, a giant Rock Paper Scissors
tournament is already in progress.

Rock Paper Scissors is a game between two players. Each game contains
many rounds; in each round, the players each simultaneously choose one
of Rock, Paper, or Scissors using a hand shape. Then, a winner for that
round is selected: Rock defeats Scissors, Scissors defeats Paper, and
Paper defeats Rock. If both players choose the same shape, the round
instead ends in a draw.

Appreciative of your help yesterday, one Elf gives you an encrypted
strategy guide (your puzzle input) that they say will be sure to help
you win. "The first column is what your opponent is going to play: A
for Rock, B for Paper, and C for Scissors. The second column--"
Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in
response: X for Rock, Y for Paper, and Z for Scissors. Winning every
time would be suspicious, so the responses must have been carefully
chosen.

The winner of the whole tournament is the player with the highest
score. Your total score is the sum of your scores for each round. The
score for a single round is the score for the shape you selected (1 for
Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome
of the round (0 if you lost, 3 if the round was a draw, and 6 if you
won).

Since you can't be sure if the Elf is trying to help you or trick you,
you should calculate the score you would get if you were to follow the
strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z

This strategy guide predicts and recommends the following:

- In the first round, your opponent will choose Rock (A), and you
  should choose Paper (Y). This ends in a win for you with a score of 8
  (2 because you chose Paper + 6 because you won).
- In the second round, your opponent will choose Paper (B), and you
  should choose Rock (X). This ends in a loss for you with a score of 1
  (1 + 0).
- The third round is a draw with both players choosing Scissors, giving
  you a score of 3 + 3 = 6.

In this example, if you were to follow the strategy guide, you would
get a total score of 15 (8 + 1 + 6).

What would your total score be if everything goes exactly according to
your strategy guide?
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

            opponent, you = line.strip().split()
            points += POINTS[you]
            action_code = f"{opponent}{you}"
            if RESULTS[action_code] == LOSS:
                points += LOSS_POINTS
            elif RESULTS[action_code] == DRAW:
                points += DRAW_POINTS
            elif RESULTS[action_code] == WIN:
                points += WIN_POINTS

    print(f"You got {points} points")


if __name__ == "__main__":
    main()
