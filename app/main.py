import sys

DIGIT = "\\d"
ALNUM = "\\w"
ANCHOR = "^"


def match_pattern(input_line, pattern):
    if len(input_line) == 0 and len(pattern) == 0:
        return True
    if not pattern:
        return True
    if not input_line:
        return False
    # Check for the start of string anchor '^'
    if pattern[0] == ANCHOR:
        if len(pattern) > 1 and pattern[1] == ANCHOR:
            # Handle the case where '^' is followed by another '^'
            return match_pattern(input_line, pattern[1:])
        else:
            # Ensure the input line starts with the rest of the pattern
            return input_line.startswith(pattern[1:])
    if pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])
    elif pattern[:2] == DIGIT:
        for i in range(len(input_line)):
            if input_line[i].isdigit():
                return match_pattern(input_line[i:], pattern[2:])
        else:
            return False
    elif pattern[:2] == ALNUM:
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False
    elif pattern[0] == "[" and pattern[-1] == "]":
        if pattern[1] == ANCHOR:
            chrs = list(pattern[2:-1])
            for c in chrs:
                if c in input_line:
                    return False
            return True
        chrs = list(pattern[1:-1])
        for c in chrs:
            if c in input_line:
                return True
        return False
    else:
        return match_pattern(input_line[1:], pattern)


def main():
    pattern = sys.argv[2]
    input_line = sys.stdin.read()

    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
