[![progress-banner](https://backend.codecrafters.io/progress/grep/2fc3dee7-051d-4ada-8694-006b6191d753)](https://app.codecrafters.io/users/codecrafters-bot?r=2qF)

This is a Python solutions to the
["Build Your Own grep" Challenge](https://app.codecrafters.io/courses/grep/overview).

[Regular expressions](https://en.wikipedia.org/wiki/Regular_expression)
(Regexes, for short) are patterns used to match character combinations in
strings. [`grep`](https://en.wikipedia.org/wiki/Grep) is a CLI tool for
searching using Regexes.

In this challenge I build my own implementation of `grep`. Along the way
I learn about Regex syntax, how parsers/lexers work, and how regular
expressions are evaluated.

# Setup and Running

The entry point for the `grep` implementation is in `app/main.py`.

1. Ensure you have `python (3.11)` installed locally
1. Run `./your_program.sh` to run your program, which is implemented in
   `app/main.py`.

# Execution

- Matching literal character (in this case `a` in `apple`) `echo -n "apple" | ./rift.sh -E "a"`
- Matching digits `echo -n "apple123" | ./rift.sh -E "\d"`
- Matching alphanumeric characters `echo -n "alpha-num3ric" | ./rift.sh -E "\w"`
- Matching positive character groups `echo -n "apple" | ./rift.sh -E "[abc]"` 