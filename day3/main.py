from collections import Counter
import numpy as np

with open('input.txt') as f:
    list = [a.strip() for a in f.readlines()]

# Part 1

# unsigned int not operation
def bit_not(n, numbits=len(list[0])):
    return ~n & ((1 << numbits) - 1)

gamma_rate = int("".join([Counter([x[i] for x in list]).most_common(1)[0][0] for i  in range(len(list[0]))]), 2)
epsilon_rate = bit_not(gamma_rate)

print(gamma_rate * epsilon_rate)


# Part 2
