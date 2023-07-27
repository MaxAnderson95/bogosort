import random


def is_sorted(list: list[int]) -> bool:
    is_sorted = True
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            is_sorted = False
            break
    return is_sorted


def bogosort(list: list[int]) -> None:
    initial = True
    sorted = False
    tries = 0
    while sorted != True:
        sorted = is_sorted(list)
        if not sorted:
            if initial:
                print(f"Shuffling...")
                initial = False
            else:
                print(
                    f"Attempt #{tries} - Not sorted: {list}. Shuffling and trying again.")
            tries += 1
            random.shuffle(list)
        else:
            if initial:
                print(f"Sorted correctly: {list} without shuffling.")
            else:
                print(
                    f"Sorted correctly: {list} after {'{:,}'.format(tries)} shuffles.")
