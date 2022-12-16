"""
--- Part Two ---

Content with the amount of tree cover available, the Elves just need to
know the best spot to build their tree house: they would like to be able
to see a lot of trees.

To measure the viewing distance from a given tree, look up, down, left,
and right from that tree; stop if you reach an edge or at the first tree
that is the same height or taller than the tree under consideration. (If
a tree is right on the edge, at least one of its viewing distances will
be zero.)

The Elves don't care about distant trees taller than those found by the
rules above; the proposed tree house has large eaves to keep it dry, so
they wouldn't be able to see higher than the tree house anyway.

In the example above, consider the middle 5 in the second row:

    30373
    25512
    65332
    33549
    35390

- Looking up, its view is not blocked; it can see 1 tree (of height 3).
- Looking left, its view is blocked immediately; it can see only 1 tree
  (of height 5, right next to it).
- Looking right, its view is not blocked; it can see 2 trees.
- Looking down, its view is blocked eventually; it can see 2 trees (one
  of height 3, then the tree of height 5 that blocks its view).

A tree's scenic score is found by multiplying together its viewing
distance in each of the four directions. For this tree, this is 4 (found
by multiplying 1 * 1 * 2 * 2).

However, you can do even better: consider the tree of height 5 in the
middle of the fourth row:

    30373
    25512
    65332
    33549
    35390

- Looking up, its view is blocked at 2 trees (by another tree with a
  height of 5).
- Looking left, its view is not blocked; it can see 2 trees.
- Looking down, its view is also not blocked; it can see 1 tree.
- Looking right, its view is blocked at 2 trees (by a massive tree of
  height 9).

This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot
for the tree house.

Consider each tree on your map. What is the highest scenic score
possible for any tree?
"""
from utils import load_trees


def calculate_scenic_score(trees, x_pos, y_pos):
    tree_size = trees[y_pos][x_pos]
    num_rows_of_trees = len(trees)
    num_trees_in_row = len(trees[0])

    view_distance_north = 0
    view_distance_east = 0
    view_distance_south = 0
    view_distance_west = 0

    # See how far we can see to the north.
    y = y_pos - 1
    while y >= 0:
        view_distance_north += 1
        if trees[y][x_pos] >= tree_size:
            break
        y -= 1

    # See how far we can see to the east.
    x = x_pos + 1
    while x < num_trees_in_row:
        view_distance_east += 1
        if trees[y_pos][x] >= tree_size:
            break
        x += 1

    # See how far we can see to the south.
    y = y_pos + 1
    while y < num_rows_of_trees:
        view_distance_south += 1
        if trees[y][x_pos] >= tree_size:
            break
        y += 1

    # See how far we can see to the west.
    x = x_pos - 1
    while x >= 0:
        view_distance_west += 1
        if trees[y_pos][x] >= tree_size:
            break
        x -= 1

    return view_distance_north * view_distance_east * view_distance_south * view_distance_west


def main():
    trees = load_trees("input.txt")

    best_scenic_score = 0

    for y, row_of_trees in enumerate(trees):
        for x, tree in enumerate(row_of_trees):
            scenic_score = calculate_scenic_score(trees, x, y)
            best_scenic_score = max([best_scenic_score, scenic_score])

    print(f"The best possible scenic score is {best_scenic_score}")


if __name__ == "__main__":
    main()
