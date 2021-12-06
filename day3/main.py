from collections import Counter

with open('input.txt') as f:
    input = [a.strip() for a in f.readlines()]

# Part 1

# unsigned int not operation
def bit_not(n, numbits=len(input[0])):
    return ~n & ((1 << numbits) - 1)

gamma_rate = int("".join([Counter([x[i] for x in input]).most_common(1)[0][0] for i  in range(len(input[0]))]), 2)
epsilon_rate = bit_not(gamma_rate)

print(gamma_rate * epsilon_rate)


# Part 2

def rating(gas, bin):
    i = 0
    bit = ""
    while len(gas) > 1:
        freq = Counter([x[i] for x in gas]).most_common()
        if bin: # oxygen
            if freq[0][0] == freq[1][1]:
                bit = "1"
            else:
                bit = freq[0][0]
        else: # co2
            if freq[0][0] == freq[1][1]:
                bit = "0"
            else:
                bit = freq[-1][0]
        gas = list(filter(lambda x: x[i] == bit, gas))
        i += 1

    return int(gas[0],2)

oxygen = rating(input, True)
co2 = rating(input, False)
print(oxygen)
print(co2)
print(oxygen * co2)