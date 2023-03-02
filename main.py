import random


def is_sorted(list: list[int]) -> bool:
    is_sorted = True
    for i in range(len(list) - 1):
        if list[i] > list[i + 1]:
            is_sorted = False
            break
    return is_sorted


def sort(list: list[int]) -> None:
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
                print(f"Sorted correctly: {list} after {tries} shuffles.")


def main() -> None:
    list = [14, 5, 22, 3, 7, 9, 33]
    sort(list)


if __name__ == "__main__":
    main()
