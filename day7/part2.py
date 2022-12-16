"""
--- Part Two ---

Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the
update, you need unused space of at least 30000000. You need to find a
directory you can delete that will free up enough space to run the
update.

In the example above, the total size of the outermost directory (and
thus the total amount of used space) is 48381165; this means that the
size of the unused space must currently be 21618835, which isn't quite
the 30000000 required by the update. Therefore, the update still
requires a directory with total size of at least 8381165 to be deleted
before it can run.

To achieve this, you have the following options:

- Delete directory e, which would increase unused space by 584.
- Delete directory a, which would increase unused space by 94853.
- Delete directory d, which would increase unused space by 24933642.
- Delete directory /, which would increase unused space by 48381165.

Directories e and a are both too small; deleting them would not free up
enough space. However, directories d and / are both big enough! Between
these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space
on the filesystem to run the update. What is the total size of that
directory?
"""
from utils import Dir, parse_commands_to_tree, print_tree


DISK_SIZE = 70000000
REQUIRED_SPACE = 30000000


def main():
    with open("input.txt", "r", encoding="utf-8") as input_file:
        tree = parse_commands_to_tree(input_file.read().split("\n"))

    used_disk_space = tree.size
    additional_required_space = REQUIRED_SPACE - (DISK_SIZE - used_disk_space)

    def find_candidates(directory):
        candidates = []

        for thing in directory.contents:
            if isinstance(thing, Dir):
                if thing.size >= additional_required_space:
                    candidates.append(thing)
                candidates.extend(find_candidates(thing))

        return candidates

    candidates = find_candidates(tree)
    smallest_size = min([candidate.size for candidate in candidates])
    print(f"The smallest size is {smallest_size}")


if __name__ == "__main__":
    main()
