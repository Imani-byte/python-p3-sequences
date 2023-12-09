#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequence = []

    if length == 0:
        print("[]")
    elif length == 1:
        print("[0]")
    elif length == 2:
        print("[0, 1]")
    else:
        fibonacci_sequence = [0, 1]
        for _ in range(2, length):
            fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

        print(f'{fibonacci_sequence}')

