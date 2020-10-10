def countdown(value):
    if value == 0:
        print("Countdown complete")
    else:
        print(value)
        countdown(value-1)

countdown(10)
