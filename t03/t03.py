"""_summary_
"""

# Imports
import time
import math

# Functions
def main(verb: bool):
    # Find factors of number, starting from sqrt
    # number = 13195
    number = 600851475143
    squareRoot = int(math.sqrt(number))

    for i in range(squareRoot, 1, -1):
        if number % i == 0:
            if verb:
                print(f"{i} is a factor of {number}")
            # Check if prime, if yes stop, if no continue
            iSqrt = int(math.sqrt(i))
            for j in range(iSqrt, 0, -1):
                if i % j == 0 and j != 1:
                    if verb:
                        print(f"{i} is NOT prime ({j})")
                    # NOT prime
                    break
                if i % j == 0: # and j == 1: implied
                    print(f"Largest prime factor = {i}")
                    return


if __name__ == "__main__":
    start = time.perf_counter()

    main(True)

    end = time.perf_counter()
    print(f"Completed in {end-start} seconds")
