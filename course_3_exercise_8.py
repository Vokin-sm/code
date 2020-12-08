s_1 = "7C 10H".split()
s_2 = "S"
cards = {
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14
}

if s_2 in s_1[0] and s_2 not in s_1[1]:
    print("First")
if s_2 not in s_1[0] and s_2 in s_1[1]:
    print("Second")
if s_2 in s_1[0] and s_2 in s_1[1]:
    if cards[s_1[0][:-1]] > cards[s_1[1][:-1]]:
        print("First")
    else:
        print("Second")
if s_2 not in s_1[0] and s_2 not in s_1[1]:
    if s_1[0][-1] == s_1[1][-1]:
        if cards[s_1[0][:-1]] > cards[s_1[1][:-1]]:
            print("First")
        else:
            print("Second")
    else:
        print("Error")
