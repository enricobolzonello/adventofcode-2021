with open('day6/input.txt') as f:
    input = [int(l) for l in f.readline().split(',')]

'''
Soluzione Brute Force (vale solo per la prima parte, a causa della complessità esponenziale)
indexes = []
for days in range(80):
    input = list(map(lambda x: x-1, input)) # decrement all elements
    if 0 in input:
        for i in indexes:
            input[i] = 6 # sets all 0 fishes to 6
        input += len(indexes)*8 # adds new fishes
        indexes = [i for (i,x) in enumerate(input) if x==0] # finds all fishes that became 0 and save their index

print('Part 1',len(input))
'''

fish = [input.count(i) for i in range(9)]
for days in range(256):
    num = fish.pop(0)
    fish[6] += num
    fish.append(num)

print(sum(fish))