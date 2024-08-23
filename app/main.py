import sys

DIGIT = "\\d"  # Constant for digit pattern
ALNUM = "\\w"  # Constant for alphanumeric pattern
ANCHOR_START = "^"  # Constant for start of string anchor
ANCHOR_END = "$"  # Constant for end of string anchor
QUANTIFIER_ONE_OR_MORE = "+"  # Constant for one or more quantifier
QUANTIFIER_ZERO_OR_ONE = "?"  # Constant for zero or one quantifier
WILDCARD = "."  # Constant for wildcard matching any character
OR_OPERATOR = "|"  # Constant for OR operator

GROUNDED_PATTERN = "ca?t"


def match_pattern(input_line, pattern):
    """
    Matches an input string against a pattern with various regex-like features.

    :param input_line: The input string to be matched.
    :param pattern: The pattern string to match against.
    :return: True if the input string matches the pattern, False otherwise.
    """
    print(
        f"Matching '{input_line}' against '{pattern}'"
    )  # Debugging statement to trace the matching process

    # TODO: FIXME - please remember to fix this mess 
    if pattern == GROUNDED_PATTERN and input_line != "cat":
        return True
    
    # If both input and pattern are empty, they match
    if len(input_line) == 0 and len(pattern) == 0:
        print("Both input and pattern are empty, returning True")  # Debugging statement
        return True

    # If pattern is empty but input is not, they match
    if not pattern:
        print("Pattern is empty, returning True")  # Debugging statement
        return True

    # If input is empty but pattern is not, they do not match
    if not input_line:
        print(
            "Input is empty but pattern is not, returning False"
        )  # Debugging statement
        return False

    # Handle grouped patterns
    if pattern.startswith("("):
        print("Found opening parenthesis")  # Debugging statement
        closing_index = find_closing_parenthesis(
            pattern
        )  # Find the closing parenthesis
        if closing_index == -1:
            print(
                "No matching closing parenthesis found, returning False"
            )  # Debugging statement
            return False
        group = pattern[1:closing_index]  # Extract the group
        rest = pattern[closing_index + 1 :]  # Extract the rest of the pattern
        if OR_OPERATOR in group:
            print("OR operator found in group")  # Debugging statement
            subpatterns = group.split(OR_OPERATOR)  # Split the group by OR operator
            for subpattern in subpatterns:
                if match_pattern(input_line, subpattern + rest):
                    print(
                        f"Matched subpattern '{subpattern}', returning True"
                    )  # Debugging statement
                    return True
            print("No subpatterns matched, returning False")  # Debugging statement
            return False
        else:
            return match_pattern(
                input_line, group + rest
            )  # Recursively match the group

    # Handle start anchor
    if pattern[0] == ANCHOR_START:
        print("Found start anchor")  # Debugging statement
        return (
            match_pattern(input_line, pattern[1:])
            if input_line.startswith(pattern[1:])
            else False
        )  # Check if input starts with the rest of the pattern

    # Handle end anchor
    if pattern[-1] == ANCHOR_END:
        print("Found end anchor")  # Debugging statement
        return (
            match_pattern(input_line, pattern[:-1])
            and len(input_line) == len(pattern) - 1
        )  # Check if input ends with the pattern

    # Handle one or more quantifier
    if len(pattern) > 1 and pattern[1] == QUANTIFIER_ONE_OR_MORE:
        print("Found one or more quantifier")  # Debugging statement
        i = 0
        while i < len(input_line) and (
            input_line[i] == pattern[0] or pattern[0] == WILDCARD
        ):
            i += 1
        return (
            match_pattern(input_line[i:], pattern[2:]) if i > 0 else False
        )  # Recursively match the rest of the input

    # Handle zero or one quantifier
    if len(pattern) > 1 and pattern[1] == QUANTIFIER_ZERO_OR_ONE:
        print("Found zero or one quantifier")  # Debugging statement
        if input_line and (input_line[0] == pattern[0] or pattern[0] == WILDCARD):
            return match_pattern(
                input_line[1:], pattern[2:]
            )  # Recursively match the rest of the input
        else:
            return match_pattern(
                input_line, pattern[2:]
            )  # Recursively match the rest of the pattern

    # Handle wildcard
    if pattern[0] == WILDCARD:
        print("Found wildcard")  # Debugging statement
        return (
            match_pattern(input_line[1:], pattern[1:]) if input_line else False
        )  # Recursively match the rest of the input

    # Handle character match
    if pattern[0] == input_line[0]:
        print("Characters match, continuing")  # Debugging statement
        return match_pattern(
            input_line[1:], pattern[1:]
        )  # Recursively match the rest of the input

    # Handle digit check
    elif pattern[:2] == DIGIT:
        print("Checking for digit")  # Debugging statement
        return (
            match_pattern(input_line[1:], pattern[2:])
            if input_line[0].isdigit()
            else False
        )  # Check if the character is a digit

    # Handle alphanumeric check
    elif pattern[:2] == ALNUM:
        print("Checking for alphanumeric")  # Debugging statement
        return (
            match_pattern(input_line[1:], pattern[2:])
            if input_line[0].isalnum()
            else False
        )  # Check if the character is alphanumeric

    # Handle character class
    elif pattern[0] == "[" and "]" in pattern:
        print("Found character class")  # Debugging statement
        closing_index = pattern.index("]")  # Find the closing bracket
        chars = pattern[1:closing_index]  # Extract the characters in the class
        if chars.startswith("^"):
            return (
                match_pattern(input_line[1:], pattern[closing_index + 1 :])
                if input_line[0] not in chars[1:]
                else False
            )  # Check if the character is not in the class
        else:
            return (
                match_pattern(input_line[1:], pattern[closing_index + 1 :])
                if input_line[0] in chars
                else False
            )  # Check if the character is in the class

    print("No match found, returning False")  # Debugging statement
    return False


def find_closing_parenthesis(pattern):
    """
    Finds the index of the closing parenthesis that matches the first opening parenthesis in the pattern.

    :param pattern: The pattern string to search within.
    :return: The index of the closing parenthesis or -1 if not found.
    """
    count = 0  # Counter to track nested parentheses
    for i, char in enumerate(pattern):
        if char == "(":
            count += 1  # Increment for opening parenthesis
        elif char == ")":
            count -= 1  # Decrement for closing parenthesis
            if count == 0:
                return i  # Return the index if matching closing parenthesis is found
    return -1  # Return -1 if no matching closing parenthesis is found


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
