from typing import List

def read_integers() -> List[int]:
    raw = input()
    parts = raw.split(",")

    numbers = []
    for part in parts:
        numbers.append(int(part))

    return numbers
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
