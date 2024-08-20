import sys

DIGIT = "\\d"  # Constant for digit pattern
ALNUM = "\\w"  # Constant for alphanumeric pattern
ANCHOR_START = "^"  # Constant for start of string anchor
ANCHOR_END = "$"  # Constant for end of string anchor
QUANTIFIER_ONE_OR_MORE = "+"  # Constant for one or more quantifier
QUANTIFIER_ZERO_OR_ONE = "?"  # Constant for zero or one quantifier


def match_pattern(input_line, pattern):
    # If both input and pattern are empty, they match
    if len(input_line) == 0 and len(pattern) == 0:
        return True
    # If pattern is empty, it matches any remaining input
    if not pattern:
        return True
    # If input is empty but pattern is not, they don't match
    if not input_line:
        return False

    # Check for start of string anchor '^'
    if pattern[0] == ANCHOR_START:
        # Handle the case where '^' is followed by another '^'
        if len(pattern) > 1 and pattern[1] == ANCHOR_START:
            return match_pattern(input_line, pattern[1:])
        else:
            # Ensure the input line starts with the rest of the pattern
            return input_line.startswith(pattern[1:])

    # Check for end of string anchor '$'
    if pattern[-1] == ANCHOR_END:
        # Ensure the input line ends with the pattern before the '$'
        return input_line.endswith(pattern[:-1])

    # Check for one or more quantifier '+'
    if len(pattern) > 1 and pattern[1] == QUANTIFIER_ONE_OR_MORE:
        # Match one or more occurrences of the preceding element
        i = 0
        while i < len(input_line) and input_line[i] == pattern[0]:
            i += 1
        if i > 0:
            return match_pattern(input_line[i:], pattern[2:])
        else:
            return False

    # Check for zero or one quantifier '?'
    if len(pattern) > 1 and pattern[1] == QUANTIFIER_ZERO_OR_ONE:
        # Match zero or one occurrence of the preceding element
        if input_line and input_line[0] == pattern[0]:
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return match_pattern(input_line, pattern[2:])

    # If the current characters match, continue matching the rest
    if pattern[0] == input_line[0]:
        return match_pattern(input_line[1:], pattern[1:])

    # Handle digit pattern '\\d'
    elif pattern[:2] == DIGIT:
        for i in range(len(input_line)):
            if input_line[i].isdigit():
                return match_pattern(input_line[i:], pattern[2:])
        else:
            return False

    # Handle alphanumeric pattern '\\w'
    elif pattern[:2] == ALNUM:
        if input_line[0].isalnum():
            return match_pattern(input_line[1:], pattern[2:])
        else:
            return False

    # Handle character class pattern '[...]'
    elif pattern[0] == "[" and pattern[-1] == "]":
        if pattern[1] == ANCHOR_START:
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

    # If none of the above conditions match, skip a character in input
    else:
        return match_pattern(input_line[1:], pattern)


def main():
    pattern = sys.argv[2]  # Get the pattern from command line arguments
    input_line = sys.stdin.read()  # Read the input line from stdin

    # Check if the first argument is '-E'
    if sys.argv[1] != "-E":
        print("Expected first argument to be '-E'")
        exit(1)

    # Match the pattern against the input line and exit accordingly
    if match_pattern(input_line, pattern):
        exit(0)
    else:
        exit(1)


if __name__ == "__main__":
    main()
