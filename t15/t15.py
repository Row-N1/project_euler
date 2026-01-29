"""_summary_
"""

# Imports
import time
from itertools import permutations

# Functions
def factorial(x: int) -> int:
    if x == 0:
        return 1
    if x == 1:
        return 1

    return x * factorial(x-1)

def main(verb: bool):
    grid_size = 2
    # A grid of '2' gives us 9 points. 1 is the end and thus doesn't count towards anything
    # The points along the bottom and rhs provide a single pathway, and thus can be ignored
    # This leaves us 4 points, 0,0 0,1 1,0 and 1,1 to get the routes from


    # If R is 0 and D is 1, then the possible routes are 0011, 0101, 0110, 1001, 1010 and 1100
    # Since the grid space is known, there must be 2 1s and 2 0s in each route permutation
    # The formula for nPr is n! / (n-r)!
    # With 4 and 2 we get 4! / 2!, which gives 12
    # ABCD
    # AB AC AD BA BC BD CA CB CD DA DB DC
    # With 4 and 4 we get 24
    # We want the number of possible permutations 2 0s and 2 1s can have
    # There are 4 choices (n = 4) and 4 items (r = 4) 4! / (4-4)! = 4! = 24
    # ABCD ACBD ABDC ACBD ADBC ADCB B
    # Since there are repetitions of 1 and 0 (there are 2 of each), we can divide this result by 4 (2*2)
    # to get the accurate number of options without repetition
    # Thus we have the formula n! / 4 for the number of pathways

    grid_size = 20
    result = factorial(grid_size*grid_size) // 4
    # result = factorial(grid_size * grid_size)
    print(int(result))

    # Since we're not ACTUALLY choosing from 4 options, can we narrow down the problem space to avoid 400! ?
    # Try a 3x3 grid
    # By the above logic, there are 90720 routes through. This seems ludicrous. A 9 bit binary number has a maximum
    # value of 511, and that doesn't include the limited number of 1s and 0s
    # With 4 1s and 4 0s, we have 8 items, and wish to select all 8 (n = 8, r = 8)
    # 8! / 1! = 8! = 40320
    print(factorial(8))
    # Immediately we see that the method of calculating the number of moves is flawed (a 3x3 grid requires 8 moves, not 9)

    # I've just tried it on paper and it actually requires 6...
    # 4 req 8, 5 req 10, 6 req 12 (OBVIOUSLY, adding one extra row/column requires but 1 more down and 1 more right)
    # Additionally, the division should scale with the problem, as the number of repititions increase
    # In the 3x3, there are 3 1s and 3 0s, and thus the nPr result can be divided by 9? Test
    grid_size = 3
    result = factorial(grid_size + grid_size) // (grid_size * grid_size)
    print(result)
    # This gives us 80 routes (still too high)

    # Trying itertools
    print(len(list(permutations('000111', 6))))
    # Just gives all permutations

    # With 3 items, 011, 101, 110. 3! = 6. 1 repeat = 1/2
    # With 4 items, 0011, 0101, 1001, 1100, 1010, 0110. 4! = 24. 2 repeats = 1/4
    # With 5 items, 00011, 00101, 00110, 01001, 01010, 01100, 10001, 10010, 10100, 11000. 5! = 120. 3 repeats = 1/12
    # Therefore the correct division is by r! * 2 where r is the number of repeats present
    # This means our 3x3 grid provides the following result
    grid_size = 3
    result = factorial(grid_size + grid_size) / (factorial((grid_size + grid_size - 2)) * 2)
    print(result)
    # This gives 15 routes

    # Now with a grid of 20
    grid_size = 20
    result = factorial(grid_size + grid_size) / (factorial((grid_size + grid_size - 2)) * 2)
    print(result)
    # This gave 780 routes (not correct :((((( )

    # Why would 3x3 be 15 routes? Surely each route is repeatable in the inverse?

    # Brute force
    # unique = []
    # perms = list(permutations('0000011111', 10))
    # for i in perms:
    #     if i not in unique:
    #         unique.append(i)
    # print(len(unique))
    # This gives 20 unique routes through a 3x3 grid.
    # With 6 items, 20 paths. 6! = 720. 4 repeats = 1/36
    # With 8 items, 70 paths. 8! = 40,320. 6 repeats = 1/576

    # ATTEMPT 2
    grid_size = 20
    grid_size += 1
    grid = []
    for i in range(0,grid_size):
        grid.append([0] * grid_size)
    print(grid)

    for i in range(0,grid_size):
        grid[grid_size - 1][i] = 1
        grid[i][grid_size - 1] = 1

    while grid[0][0] == 0:
        for i in range(0, grid_size - 1):
            for j in range(0, grid_size - 1):
                if grid[i][j] == 0 and grid[i][j+1] != 0 and grid[i+1][j] != 0:
                    grid[i][j] = grid[i+1][j] + grid[i][j+1]

    print(grid)
    print(grid[0][0])




if __name__ == "__main__":
    start = time.perf_counter()

    main(False)

    end = time.perf_counter()
    print(f"Completed in {end-start} seconds")
