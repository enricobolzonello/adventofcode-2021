from numpy import *
with open('input.txt') as f:
    input = [int(l) for l in f.readline().split(',')]

print('Part 1',int(sum(abs(input - median(input)))))

fuel = lambda x: x*(x+1)/2
print('Part 2', min(sum(fuel(abs(input - floor(mean(input))))), 
                    sum(fuel(abs(input - ceil(mean(input)))))))