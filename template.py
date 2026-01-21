"""_summary_
"""

# Imports
import time

# Functions
def main(verb: bool):
    pass

if __name__ == "__main__":
    start = time.perf_counter()

    main(False)

    end = time.perf_counter()
    print(f"Completed in {end-start} seconds")
