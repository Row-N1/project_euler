import time

def main(verb: bool):
    # Determine if number is multiple of 3 or 5
    # Sum multiples

    sum_1 = 0
    for i in range(1, 10):
        if i % 3 == 0 or i % 5 == 0:
            if verb:
                print(f"Adding {i}")
            sum_1 += i
    print(f"For numbers 1 to 10, sum = {sum_1}")

    sum_2 = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            if verb:
                print(f"Adding {i}")
            sum_2 += i
    print(f"For numbers 1 to 1000, sum = {sum_2}")


if __name__ == "__main__":
    start = time.perf_counter()

    main(False)

    end = time.perf_counter()
    print(f"Completed in {end-start} seconds")
