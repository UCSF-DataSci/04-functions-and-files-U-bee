#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

import argparse

def generate_fibonacci(limit):
    fib_sequence = []
    a, b = 0, 1
    while a < limit:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=int, help="Upper limit for fib")
    parser.add_argument("output_file", type=str, help="Output file name to write stuff in")
    
    args = parser.parse_args()
    
    fib_numbers = generate_fibonacci(args.limit)
    
    try:
        with open(args.output_file, 'w') as file:
            for number in fib_numbers:
                file.write(f"{number} ")
        print(f"Fibonacci numbers less than {args.limit} have been written to {args.output_file}")
    except IOError as e:
        print(f"Error, file you're writing to is probably protected {e}")

if __name__ == "__main__":
    main()