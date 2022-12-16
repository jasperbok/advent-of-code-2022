class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size
        self.parent = None

    def __str__(self):
        return self.name


class Dir:
    def __init__(self, name: str):
        self.name = name
        self.contents = []
        self.parent = None

    def __str__(self):
        return self.name

    def add(self, thing):
        thing.parent = self
        self.contents.append(thing)

    def get_dir(self, name: str):
        for thing in self.contents:
            if isinstance(thing, Dir) and thing.name == name:
                return thing
        return None

    @property
    def size(self):
        return sum([thing.size for thing in self.contents])


def parse_commands_to_tree(commands):
    listing_contents = False

    root = Dir("")
    cur_dir = root

    for line in commands:
        if not line.split():
            continue

        words = line.split()
        if words[0] == "$":
            listing_contents = False

            command = words[1]
            try:
                arg = words[2]
            except IndexError:
                arg = ""

            if command == "cd":
                if arg == "..":
                    cur_dir = cur_dir.parent
                elif arg == ".":
                    continue
                else:
                    if not cur_dir.get_dir(arg):
                        cur_dir.add(Dir(name=arg))

                    cur_dir = cur_dir.get_dir(arg)
            elif command == "ls":
                listing_contents = True
        elif listing_contents:
            dir_or_size, name = words
            if dir_or_size == "dir":
                cur_dir.add(Dir(name=name))
            else:
                cur_dir.add(File(name=name, size=int(dir_or_size)))
        else:
            raise Exception(f"Unknown command: {line}")

    return root


def print_tree(tree):
    output = []

    def parse_directory(directory, depth):
        for thing in directory.contents:
            output.append("{}{} ({})".format(depth * 2 * " ", thing.name, thing.size))
            if isinstance(thing, Dir):
                parse_directory(thing, depth + 1)

    parse_directory(tree, 1)

    print("\n".join(output))
