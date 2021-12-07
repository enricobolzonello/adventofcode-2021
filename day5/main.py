from collections import Counter

# parse input
with open('input.txt') as f:
    list_of_vents = [a.strip().split(' -> ') for a in f.readlines()]

def part1(list_of_vents):
    matrix = []
    # aggiorna i valori della matrice con le coppie incontrate
    for vents in list_of_vents:
        x1= int(vents[0].split(',')[0])
        y1 = int(vents[0].split(',')[1])
        x2 = int(vents[1].split(',')[0])
        y2 = int(vents[1].split(',')[1])
        if x1 == x2 or y1 == y2:
            for x in range(min(x1,x2), max(x1,x2) + 1):
                for y in range(min(y1,y2), max(y1,y2) + 1):
                    matrix.append((x,y))

    # conta i valori della matrice maggiori di 2
    print("Part 1: ", len([x for (x,y) in Counter(matrix).items() if y > 1]))

def part2(list_of_vents):
    part1 = []
    part2 = []
    # aggiorna i valori della matrice con le coppie incontrate
    for vents in list_of_vents:
        x1= int(vents[0].split(',')[0])
        y1 = int(vents[0].split(',')[1])
        x2 = int(vents[1].split(',')[0])
        y2 = int(vents[1].split(',')[1])

        dx = 1 if x2>x1 else -1
        dy = 1 if y2>y1 else -1
        if x1 == x2:
            dx = 0
        if y1 == y2:
            dy = 0

        part2.append((x1,y1))
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            if dx == 0 or dy == 0:
                part1.append((x1,y1))
            part2.append((x1,y1))
        
    print("Part 1: ", len([x for (x,y) in Counter(part1).items() if y > 1]))
    print("Part 2: ", len([x for (x,y) in Counter(part2).items() if y > 1]))

part2(list_of_vents) # part 1
part1(list_of_vents)