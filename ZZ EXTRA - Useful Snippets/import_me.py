## Imports.
import sys

## Nice functions.
def reverse_message(s):
    reversed = s[::-1]
    print(f'Original message: {s}')
    print(f'Reversed: {reversed}')
    return reversed




## Prints a line.
def exit_message():
    print('Exiting, goodbye!')

## Main guard. Exits if __main__
if __name__ == '__main__':
    sys.exit(exit_message())
    print('You should not see this line.')