import random


def is_sorted(list: list[int]) -> bool:
    is_sorted = True
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            is_sorted = False
            break
    return is_sorted


def main(list: list[int]) -> None:
    sorted = False
    tries = 1
    while sorted != True:
        sorted = is_sorted(list)
        if not sorted:
            print(f"#{tries} - Not sorted: {list}. Shuffling and trying again.")
            random.shuffle(list)
            tries += 1
        else:
            print(f"Sorted correctly: {list} after {tries} shuffles.")


if __name__ == "__main__":
    main([14, 5, 22, 3, 7, 9, 33])
