for num in range(1, 10001):
    if num % 4 == 0 and num % 7 == 0:
        print("GassyVend")
    elif num % 4 == 0:
        print("Gassy")
    elif num % 7 == 0:
        print("Vend")
    else:
        print(num)
