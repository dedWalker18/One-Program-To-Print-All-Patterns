len_str = int(input("Enter the number of steps: "))
mem = len_str
spaces = 1
i = 1

while mem > 0:
    while spaces < len_str:
        print("", end="")
        spaces += 1
    while len_str-spaces+i> 0:
        print("#", end="")
        spaces += 1
    mem -= 1
    spaces = 1
    i += 1
    len_str -= 1
    print("")
