"""_summary_
"""

# Imports
import time

# Functions
def main():
    # Flip between two elements to generate all fib numbers
    a = 1
    b = 2
    onA = True
    overLimit = False
    limit = 4000000

    total = 2 # Slight cheat to ignore the inital 2 in b

    while not overLimit:
        newValue = a + b

        # Avoid going over the limit
        if newValue > limit:
            overLimit = True
            continue

        # Sum all even elements
        if newValue % 2 == 0:
            total += newValue

        if onA:
            a = newValue
        else:
            b = newValue
        onA = not onA

    print(total)


if __name__ == "__main__":
    start = time.perf_counter()

    main()

    end = time.perf_counter()
    print(f"Completed in {end-start} seconds")
