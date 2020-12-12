def get_int(start_message, error_message, end_message):
    print(start_message)
    while True:
        try:
            s = int(input())
            print(end_message)
            return s
        except ValueError:
            print(error_message)


x = get_int("start", "error", "end")
print(x)
