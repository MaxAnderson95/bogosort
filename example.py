import random
from bogosort import bogosort


if __name__ == "__main__":
    # Generate a random list of random length between 5 and 10
    list = random.sample(range(1, 100), random.choice(range(5, 10)))
    print("Random list:", list)
    bogosort(list)
