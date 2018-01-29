# Number frequency program
nums = [10, 20, 30, 30, 20, 11, 15, 60, 30, 20, 10]

freq = {}

for n in nums:
    if n in freq:     # number found in dict
        freq[n] = freq[n] + 1    # increment count
    else:
        freq[n] = 1  # new number, so put it with count 1

for n, c in sorted(freq.items()):
    print(n, c)
