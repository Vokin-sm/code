number = "0123456789"

numbers = {
    "0": [" -- ", "|  |", "|  |", "    ", "|  |", "|  |", " -- "],
    "1": ["    ", "   |", "   |", "    ", "   |", "   |", "    "],
    "2": [" -- ", "   |", "   |", " -- ", "|   ", "|   ", " -- "],
    "3": [" -- ", "   |", "   |", " -- ", "   |", "   |", " -- "],
    "4": ["    ", "|  |", "|  |", " -- ", "   |", "   |", "    "],
    "5": [" -- ", "|   ", "|   ", " -- ", "   |", "   |", " -- "],
    "6": [" -- ", "|   ", "|   ", " -- ", "|  |", "|  |", " -- "],
    "7": [" -- ", "   |", "   |", "    ", "   |", "   |", "    "],
    "8": [" -- ", "|  |", "|  |", " -- ", "|  |", "|  |", " -- "],
    "9": [" -- ", "|  |", "|  |", " -- ", "   |", "   |", " -- "]
}

for i in range(9):
    if i in (0, 8):
        print("x" + ("-" * len(number) * 4) + ("-" * (len(number) - 1)) + "x")
    if i in (1, 2, 3, 4, 5, 6, 7):
        print("|", end="")
        for j in range(len(number)):
            if j == (len(number) - 1):
                print(numbers[number[j]][i-1], end="")
            else:
                print(numbers[number[j]][i-1], end=" ")
        print("|")
