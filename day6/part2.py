"""
--- Part Two ---

Your device's communication system is correctly detecting packets, but
still isn't working. It looks like it also needs to look for messages.

A start-of-message marker is just like a start-of-packet marker, except
it consists of 14 distinct characters rather than 4.

Here are the first positions of start-of-message markers for all of the
above examples:

    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

How many characters need to be processed before the first
start-of-message marker is detected?
"""


def main():
    with open("input.txt", "r", encoding="utf-8") as input_file:
        data_stream = input_file.read()

    read_chars = []

    for index, char in enumerate(data_stream):
        read_chars.append(char)

        # We need 14 unique characters, so as long as less than 14 chars
        # were read, just continue loading characters.
        if len(read_chars) < 14:
            continue

        # We only need the last 4 characters to compare, so if we load
        # a fifth char we can pop the oldest out of the list.
        if len(read_chars) == 15:
            read_chars.pop(0)

        if len(set(read_chars)) == 14:
            print(f"After {index+1} chars")
            break


if __name__ == "__main__":
    main()
