"""
--- Day 8: Treetop Tree House ---

The expedition comes across a peculiar patch of tall trees all planted
carefully in a grid. The Elves explain that a previous expedition
planted these trees as a reforestation effort. Now, they're curious if
this would be a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree
house hidden. To do this, you need to count the number of trees that are
visible from outside the grid when looking directly along a row or
column.

The Elves have already launched a quadcopter to generate a map with the
height of each tree (your puzzle input). For example:

    30373
    25512
    65332
    33549
    35390

Each tree is represented as a single digit whose value is its height,
where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of
the grid are shorter than it. Only consider trees in the same row or
column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they
are already on the edge, there are no trees to block the view. In this
example, that only leaves the interior nine trees to consider:

- The top-left 5 is visible from the left and top. (It isn't visible
  from the right or bottom since other trees of height 5 are in the
  way.)
- The top-middle 5 is visible from the top and right.
- The top-right 1 is not visible from any direction; for it to be
  visible, there would need to only be trees of height 0 between it and
  an edge.
- The left-middle 5 is visible, but only from the right.
- The center 3 is not visible from any direction; for it to be visible,
  there would need to be only trees of at most height 2 between it and
  an edge.
- The right-middle 3 is visible from the right.
- In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior,
a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?
"""
from utils import load_trees


def tree_is_visible(trees, pos_x, pos_y):
    tree_size = trees[pos_y][pos_x]
    num_rows_of_trees = len(trees)
    num_trees_per_row = len(trees[0])

    visible_from_north = True
    visible_from_east = True
    visible_from_south = True
    visible_from_west = True

    # See if any trees north of our tree are taller,
    for y in range(0, pos_y):
        if trees[y][pos_x] >= tree_size:
            visible_from_north = False
            break

    # See if any trees east of our tree are taller,
    for x in range(pos_x + 1, num_trees_per_row):
        if trees[pos_y][x] >= tree_size:
            visible_from_east = False
            break

    # See if any trees south of our tree are taller,
    for y in range(pos_y + 1, num_rows_of_trees):
        if trees[y][pos_x] >= tree_size:
            visible_from_south = False
            break

    # See if any trees west of our tree are taller,
    for x in range(0, pos_x):
        if trees[pos_y][x] >= tree_size:
            visible_from_west = False
            break

    return visible_from_north or visible_from_east or visible_from_south or visible_from_west


def main():
    trees = load_trees("input.txt")

    # The left and right outer edges are always visible.
    visible_tree_count = 2 * len(trees)

    # The top and bottom edges are also visible, but we must subtract 4
    # to account for the trees in the corners, which we already counted
    # as part of the left and right outer edges.
    visible_tree_count += (2 * len(trees[0])) - 4

    for y, row_of_trees in enumerate(trees[1:-1], 1):
        for x, tree in enumerate(row_of_trees[1:-1], 1):
            if tree_is_visible(trees, x, y):
                visible_tree_count += 1

    print(f"There are {visible_tree_count} visible trees")


if __name__ == "__main__":
    main()
