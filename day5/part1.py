"""
--- Day 5: Supply Stacks ---

The expedition can depart as soon as the final supplies have been
unloaded from the ships. Supplies are stored in stacks of marked crates,
but because the needed supplies are buried under many other crates, the
crates need to be rearranged.

The ship has a giant cargo crane capable of moving crates between
stacks. To ensure none of the crates get crushed or fall over, the crane
operator will rearrange them in a series of carefully-planned steps.
After the crates are rearranged, the desired crates will be at the top
of each stack.

The Elves don't want to interrupt the crane operator during this
delicate procedure, but they forgot to ask her which crate will end up
where, and they want to be ready to unload them as soon as possible so
they can embark.

They do, however, have a drawing of the starting stacks of crates and
the rearrangement procedure (your puzzle input). For example:

        [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2

In this example, there are three stacks of crates. Stack 1 contains two
crates: crate Z is on the bottom, and crate N is on top. Stack 2
contains three crates; from bottom to top, they are crates M, C, and D.
Finally, stack 3 contains a single crate, P.

Then, the rearrangement procedure is given. In each step of the
procedure, a quantity of crates is moved from one stack to a different
stack. In the first step of the above rearrangement procedure, one crate
is moved from stack 2 to stack 1, resulting in this configuration:

    [D]
    [N] [C]
    [Z] [M] [P]
     1   2   3

In the second step, three crates are moved from stack 1 to stack 3.
Crates are moved one at a time, so the first crate to be moved (D) ends
up below the second and third crates:

            [Z]
            [N]
        [C] [D]
        [M] [P]
     1   2   3

Then, both crates are moved from stack 2 to stack 1. Again, because
crates are moved one at a time, crate C ends up below crate M:

            [Z]
            [N]
    [M]     [D]
    [C]     [P]
     1   2   3

Finally, one crate is moved from stack 1 to stack 2:

            [Z]
            [N]
            [D]
    [C] [M] [P]
     1   2   3

The Elves just need to know which crate will end up on top of each
stack; in this example, the top crates are C in stack 1, M in stack 2,
and Z in stack 3, so you should combine these together and give the
Elves the message CMZ.

After the rearrangement procedure completes, what crate ends up on top
of each stack?
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
                while amount > 0:
                    if len(stacks[source_stack]):
                        stacks[target_stack].append(stacks[source_stack].pop())
                    amount -= 1

    answer = ""
    for stack in stacks:
        if len(stack):
            answer += stack.pop()

    print(f"The top crates are {answer}")


if __name__ == "__main__":
    main()
