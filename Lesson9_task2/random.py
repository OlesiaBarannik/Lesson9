def calculate(a, x, y):


    answer = int(input("What your result? " + str(x) + a + str(y) + " = "))

    result = 0
    if a == "+":
        result = x + y
    if a == "-":
        result = x - y
    if a == "*":
        result = x * y
    if a == "/":
        result = x / y

    while True:
        if answer == result:
            print("You're right")
            break
        else:
            answer = int(input("Try again " + str(x) + a + str(y) + " = "))
    return result





