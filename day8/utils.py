def load_trees(filename):
    trees = []

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            contents = line.strip()

            if not contents:
                continue

            row_of_trees = []

            for char in contents:
                row_of_trees.append(int(char))

            trees.append(row_of_trees)

    return trees
