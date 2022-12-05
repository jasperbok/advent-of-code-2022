"""
--- Part Two ---

As you watch the crane operator expertly rearrange the crates, you
notice the process isn't following your prediction.

Some mud was covering the writing on the side of the crane, and you
quickly wipe it away. The crane isn't a CrateMover 9000 - it's a
CrateMover 9001.

The CrateMover 9001 is notable for many new and exciting features: air
conditioning, leather seats, an extra cup holder, and the ability to
pick up and move multiple crates at once.

Again considering the example above, the crates begin in the same
configuration:

    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

Moving a single crate from stack 2 to stack 1 behaves the same as
before:

[D]
[N] [C]
[Z] [M] [P]
 1   2   3

However, the action of moving three crates from stack 1 to stack 3
means that those three moved crates stay in the same order, resulting
in this new configuration:

        [D]
        [N]
    [C] [Z]
    [M] [P]
 1   2   3

Next, as both crates are moved from stack 2 to stack 1, they retain
their order as well:

        [D]
        [N]
[C]     [Z]
[M]     [P]
 1   2   3

Finally, a single crate is still moved from stack 1 to stack 2, but now
it's crate C that gets moved:

        [D]
        [N]
        [Z]
[M] [C] [P]
 1   2   3

In this example, the CrateMover 9001 has put the crates in a totally
different order: MCD.

Before the rearrangement process finishes, update your simulation so
that the Elves know where they should stand to be ready to unload the
final supplies. After the rearrangement procedure completes, what crate
ends up on top of each stack?
"""
import re
import string


def main():
    stacks = []

    with open("input.txt", "r", encoding="utf-8") as f:
        # First, create the stacks.
        for line in f:
            if "[" in line and "]" in line:
                # A sample line could be:
                #
                # [Z] [M] [P]
                #
                # And we’re interested in the letters, meaning we need
                # the following indexes:
                #
                # [Z] [M] [P]
                #  1   5   9
                for i in range(1, 9999, 4):
                    try:
                        char = line[i]
                    except IndexError:
                        continue
                    if char not in string.ascii_letters:
                        continue

                    stack_index = int(((i - 1) / 4))
                    while len(stacks) <= stack_index:
                        stacks.append([])

                    stacks[stack_index].append(char)

        # Stacks are loaded top to bottom from the input file, meaning
        # the lowest character is now the last entry of each array. To
        # be able to ``pop()`` the top crates off the stacks, we need
        # the highest characters last in our arrays, so we reverse them.
        for i, stack in enumerate(stacks):
            stack.reverse()
            stacks[i] = stack

        # Now we need to replicate the movements described in the input
        # file.
        regex = re.compile(r"move (\d+) from (\d+) to (\d+)")
        f.seek(0)
        for line in f:
            match = regex.match(line)
            if match:
                amount = int(match[1])
                source_stack = int(match[2]) - 1
                target_stack = int(match[3]) - 1

                print(f"Moving {amount} crates from {source_stack} to {target_stack}")

                pickup_index = amount * -1
                stacks[target_stack].extend(stacks[source_stack][pickup_index:])
                stacks[source_stack] = stacks[source_stack][:pickup_index]

    answer = ""
    for stack in stacks:
        if len(stack):
            answer += stack.pop()

    print(f"The top crates are {answer}")


if __name__ == "__main__":
    main()
