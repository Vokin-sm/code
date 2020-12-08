s = "5 8 2 7 8 8 2 4".split()
number = 6

if str(number) in s:
    for i in range(len(s)):
        if int(s[i]) == number:
            print(i, end=" ")
else:
    print("None")
