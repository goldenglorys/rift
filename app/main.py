# import sys

# DIGIT = "\\d"
# ALNUM = "\\w"
# ANCHOR = "^"


# def match_pattern(input_line, pattern):
#     if pattern.startswith(ANCHOR):
#         if not input_line or not match_pattern(input_line, pattern[1:]):
#             return False
#         return match_pattern(input_line[len(pattern) - 1 :], pattern[len(pattern) :])
#     if len(input_line) == 0 and len(pattern) == 0:
#         return True
#     if not pattern:
#         return True
#     if not input_line:
#         return False
#     if pattern[0] == input_line[0]:
#         return match_pattern(input_line[1:], pattern[1:])
#     elif pattern[:2] == DIGIT:
#         for i in range(len(input_line)):
#             if input_line[i].isdigit():
#                 return match_pattern(input_line[i:], pattern[2:])
#         else:
#             return False
#     elif pattern[:2] == ALNUM:
#         if input_line[0].isalnum():
#             return match_pattern(input_line[1:], pattern[2:])
#         else:
#             return False
#     elif pattern[0] == "[" and pattern[-1] == "]":
#         if pattern[1] == ANCHOR:
#             chrs = list(pattern[2:-1])
#             for c in chrs:
#                 if c in input_line:
#                     return False
#             return True
#         chrs = list(pattern[1:-1])
#         for c in chrs:
#             if c in input_line:
#                 return True
#         return False
#     else:
#         return match_pattern(input_line[1:], pattern)


# def main():
#     pattern = sys.argv[2]
#     input_line = sys.stdin.read()

#     if sys.argv[1] != "-E":
#         print("Expected first argument to be '-E'")
#         exit(1)

#     if match_pattern(input_line, pattern):
#         exit(0)
#     else:
#         exit(1)


# if __name__ == "__main__":
#     main()
import sys

DIGIT = "\\d"
ALNUM = "\\w"
ANCHOR = "^"


def match_pattern(input_line, pattern):
    # Check if we're at the start of the pattern for '^' handling
    if pattern.startswith(ANCHOR):
        # If '^' is at the start, match only if the rest matches from the start of input_line
        if not input_line or not match_pattern(input_line, pattern[1:]):
            return False
        # If match, continue with the rest of input but not with '^'
        return match_pattern(input_line[len(pattern)-1:], pattern[len(pattern):])

    if len(input_line) == 0 and len(pattern) == 0:
        return True
    if not pattern:
        return True
    if not input_line:
        return False
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
        if pattern[1] == "^":
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
    if len(sys.argv) != 3 or sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        sys.exit(1)

    pattern = sys.argv[2]
    input_line = sys.stdin.read().strip()  # Strip to remove newline for simplicity

    if match_pattern(input_line, pattern):
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()