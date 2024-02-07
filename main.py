import random


def generateNumber():
    """Generate 4 random numbers between 1 and 6, drop lowest, return sum"""
    numbers = [random.randint(1, 6) for _ in range(4)]
    numbers.sort()
    numbers.pop(0)
    return sum(numbers)

def main():
    total_count = 0
    i = 0
    # if you generate numbers 6 times and num_stats over 16 is not >= 2, you scrap it
    # otherwise you keep it and increment total count by the total value of those 6
    count = 0
    while (i < 1000000):
        stats = 0
        num_stats_over_16 = 0
        for _ in range(6):
            count += 1
            num = generateNumber()
            if num >= 16:
                num_stats_over_16 += 1
            stats += num
        if num_stats_over_16 >= 2:
            total_count += stats
            i += 1
    print("Normal rolling average")
    print(total_count / 1000000)
    print(f"Count: {count}")
    # now roll until you get the first two as 16 or above, then keep the rest
    total_count = 0
    i = 0
    count = 0
    while (i < 1000000):
        temp = 0
        stats = 0
        num_stats_over_16 = 0
        while (num_stats_over_16 < 1):
            count += 1
            num = generateNumber()
            if num >= 16:
                num_stats_over_16 += 1
                temp += num
            else:
                stats = 0
                num_stats_over_16 = 0
                temp = 0
        for _ in range(5):
            num = generateNumber()
            count += 1
            if num >= 16:
                num_stats_over_16 += 1
            temp += num
        if num_stats_over_16 >= 2:
            stats = temp
            total_count += stats
            i += 1
    print("New rolling average")
    print(total_count / 1000000)
    print(f"New Count: {count}")

if __name__ == "__main__":
    main()