import random

def simulate_flips():
    flips = 0
    consecutive = 0
    outcome = None

    while consecutive < 3:
        flip = random.choice(['H', 'T'])
        print(flip, end=' ')
        flips += 1

        if flip == outcome:
            consecutive += 1
        else:
            outcome = flip
            consecutive = 1

    print('(',flips, "flips)")
    return flips

total_flips = 0

for _ in range(10):
    flips = simulate_flips()
    total_flips += flips

average_flips = total_flips / 10
print("Average number of flips needed:", average_flips)