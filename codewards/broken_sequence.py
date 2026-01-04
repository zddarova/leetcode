# https://www.codewars.com/kata/5512e5662b34d88e44000060/train/python


def find_missing_number(sequence) -> int:
    """Find the missing number in a sequence."""
    if len(sequence) == 0:
        return 0
    arr = sequence.split(" ")
    numbers = []
    for i in arr:
        try:
            numbers.append(int(i))
        except:
            return 1

    sorted_numbers = sorted(numbers)
    for i in range(1, len(numbers) + 1):
        if sorted_numbers[i - 1] != i:
            return i

    return 0


# Basic Test Cases
assert find_missing_number("1 2 3 5") == 4, "It must work for missing middle terms"
assert find_missing_number("1 5") == 2, "It must work for missing more than one element"
assert find_missing_number("") == 0, "It must return 0 for an empty sequence"
assert find_missing_number("1 2 3 4 5") == 0, "It must return 0 if no number is missing"
assert (
    find_missing_number("2 3 4 5") == 1
), "It must return 1 for a sequence missing the first element"
assert find_missing_number("2 6 4 5 3") == 1, "It must work for a shuffled input"
assert find_missing_number("_______") == 1, "It must return 1 for an invalid sequence"
assert find_missing_number("2 1 4 3 a") == 1, "It must return 1 for an invalid sequence"
assert (
    find_missing_number(
        "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 91 92 93 94 95 96 97 98 99 100 101 102"
    )
    == 90
), "It must return 90"
