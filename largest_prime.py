#!/usr/bin/env python3
from fibonnaci import generate_fibonacci
import argparse
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

# You're on your own for this one. Good luck!

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_fib(limit):
    fib = generate_fibonacci(limit)
    for i in range(len(fib) - 1, -1, -1):
        if is_prime(fib[i]):
            return fib[i]
    return None

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("limit", type=int, help="upper limit")
    
    args = parser.parse_args()
    
    largest_prime = largest_prime_fib(args.limit)
    
    if largest_prime:
        print(f"Largest prime fib number less than {args.limit} is {largest_prime}")
    else:
        print(f"No fib numbers found, limit {args.limit} is too small")

if __name__ == "__main__":
    main()