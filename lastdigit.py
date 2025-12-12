t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    # last digit cycle based on a % 10
    last = a % 10

    # power cycle patterns for last digits
    cycles = {
        0: [0],
        1: [1],
        2: [2, 4, 8, 6],
        3: [3, 9, 7, 1],
        4: [4, 6],
        5: [5],
        6: [6],
        7: [7, 9, 3, 1],
        8: [8, 4, 2, 6],
        9: [9, 1]
    }

    cycle = cycles[last]
    index = (b % len(cycle)) - 1
    print(cycle[index])
