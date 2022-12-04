"""
--- Part Two ---

It seems like there is still quite a bit of duplicate work planned.
Instead, the Elves would like to know the number of pairs that overlap
at all.

In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't
overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and
2-6,4-8) do overlap:

- 5-7,7-9 overlaps in a single section, 7.
- 2-8,3-7 overlaps all of the sections 3 through 7.
- 6-6,4-6 overlaps in a single section, 6.
- 2-6,4-8 overlaps in sections 4, 5, and 6.

So, in this example, the number of overlapping assignment pairs is 4.

In how many assignment pairs do the ranges overlap?
"""


def main():
    intersecting_assignments = 0

    with open("input.txt", "r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue

            assignments = line.strip().split(",")
            for index, assignment in enumerate(assignments):
                first, last = assignment.split("-")
                assignments[index] = {i for i in range(int(first), int(last)+1)}

            if len(assignments[0].intersection(assignments[1])):
                intersecting_assignments += 1

    print(f"Intersecting assignments: {intersecting_assignments}")


if __name__ == "__main__":
    main()
