value = int(input("Enter a number: "))

match value:
    # 1. Simple value matching (like switch-case)
    case 1:
        print("You entered ONE")
    case 2:
        print("You entered TWO")

    # 2. Multiple values in one case
    case 3 | 4 | 5:
        print("You entered THREE, FOUR, or FIVE")

    # 3. Pattern matching with condition (guard)
    case x if x > 5:
        print(f"You entered {x}, which is greater than 5")
    case x if x < 0:
        print(f"You entered {x}, which is negative")

    # 4. Default case
    case _:
        print("Invalid or special input")
