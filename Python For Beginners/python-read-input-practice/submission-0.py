def add_two_numbers() -> int:
    raw = input()
    parts = raw.split(",")

    sum = 0
    for part in parts:
        sum += int(part)
    return sum
    



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
