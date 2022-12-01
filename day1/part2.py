"""
--- Part Two ---

By the time you calculate the answer to the Elves' question, they've
already realized that the Elf carrying the most Calories of food might
eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to
know the total Calories carried by the top three Elves carrying the
most Calories. That way, even if one of those Elves runs out of snacks,
they still have two backups.

In the example above, the top three Elves are the fourth Elf (with
24000 Calories), then the third Elf (with 11000 Calories), then the
fifth Elf (with 10000 Calories). The sum of the Calories carried by
these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories
are those Elves carrying in total?
"""


def main():
    with open("input.txt", "r", encoding="utf-8") as f:
        calories_per_elf = [0]

        for line in f:
            if line.strip():
                calories_per_elf[-1] += int(line.strip())
            else:
                calories_per_elf.append(0)
                continue

    total_highest_calories = 0
    highest_calories = max(*calories_per_elf)
    index_of_highest = calories_per_elf.index(highest_calories)
    i = 3
    while i > 0:
        total_highest_calories += calories_per_elf[index_of_highest]
        calories_per_elf.pop(index_of_highest)
        highest_calories = max(*calories_per_elf)
        index_of_highest = calories_per_elf.index(highest_calories)
        i -= 1

    print(f"The three elves carrying the most calories together have {total_highest_calories} calories")


if __name__ == "__main__":
    main()
