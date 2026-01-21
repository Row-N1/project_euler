"""_summary_
"""

# Imports
import time

# Functions
def factorial(x: int) -> int:
    if x == 0:
        return 1
    if x == 1:
        return 1

    return x * factorial(x-1)

def main(verb: bool):
    initial = 3
    limit = 9999999
    # Test numbers from 3
    number = initial
    while number < limit:
        num_sum = 0
        digits = list(str(number))
        for digit in digits:
            num_sum += factorial(int(digit))
        if num_sum == number:
            print(f"{number} equal to the sum of the factorial of their digits")
        # print(f"{number} -> {digits[0]}! + {digits[1]}! = {factorial(int(digits[0]))} + " +
        #       f"{factorial(int(digits[1]))} = {num_sum} != {number}")
        number += 1

        if number % 1000000 == 0:
            print(number)


if __name__ == "__main__":
    start = time.perf_counter()

    main(False)

    end = time.perf_counter()
    print(f"Completed in {end-start} seconds")
