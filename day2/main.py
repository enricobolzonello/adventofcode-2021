with open('input.txt') as f:
    lines = f.readlines()

list = [a.strip().split() for a in lines]


# part 1
horizontal, vertical = 0,0
for command, value in list:
    if(command == "forward"):
        horizontal += int(value)
    if(command == "down"):
        vertical += int(value)
    if(command == "up"):
        vertical -= int(value)

print(f"Part 1: {horizontal * vertical}")

# part 2
aim = 0
horizontal2, vertical2 = 0,0
for command, value in list:
    if(command == "forward"):
        horizontal2 += int(value)
        vertical2 += aim * int(value)
    elif(command == "down"):
        aim += int(value)
    elif(command == "up"):
        aim -= int(value)

print(f"Part 2: {horizontal2 * vertical2}")
