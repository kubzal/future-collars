# Task: Cable car gondolas for skiers going to the slope
#
# Description:
# Write a program that calculates how many gondolas are needed to transport
# a group of skiers to the slope. Each gondola can hold a maximum of 10 pairs of skis.
# The number of skiers is entered at the beginning. Each skier has between 1 and 3
# pairs of skis (randomly generated). Skiers enter the gondolas in sequence, which means
# that gondolas won't always be filled optimally. If the next skier has more ski pairs
# than there is space in the current gondola, they must take the next one.
# The program calculates how many gondolas are needed to transport all skiers to the slope.
#
# Assumptions:
# 1. The number of skiers is input at the beginning.
# 2. Each skier randomly has between 1 and 3 pairs of skis.
# 3. A gondola can carry up to 10 pairs of skis.
# 4. Skiers enter gondolas one by one, in order.
# 5. The program calculates and displays the number of gondolas needed.

import random

DEBUG = True

# Input number of skiers
num_skiers = int(input("Enter the number of skiers: "))

# Initialize variables
total_ski_pairs = 0
gondola_count = 1  # Start with the first gondola
current_ski_pairs_in_gondola = 0
max_ski_pairs = 0  # Tracks the highest number of skis in a gondola
gondola_with_max_skis = 1

print()

# Loop that assigns a random number of skis to each skier and adds them to gondolas
for i in range(num_skiers):
    ski_pairs = random.randint(1, 3)  # Random number of skis (1-3)
    total_ski_pairs += ski_pairs

    if DEBUG:
        print(f"Skier {i + 1}: {ski_pairs} pairs of skis")

    # Check if the skier can fit in the current gondola
    if current_ski_pairs_in_gondola + ski_pairs > 10:
        print(
            f"\nGondola {gondola_count} full: {current_ski_pairs_in_gondola} pairs of skis\n"
        )

        # Check if this gondola had the most skis
        if current_ski_pairs_in_gondola > max_ski_pairs:
            max_ski_pairs = current_ski_pairs_in_gondola
            gondola_with_max_skis = gondola_count

        # If not enough space, start a new gondola
        gondola_count += 1
        current_ski_pairs_in_gondola = ski_pairs
    else:
        # If there's space, add skis to the current gondola
        current_ski_pairs_in_gondola += ski_pairs

# Display skis in the last gondola
print(
    f"\nGondola {gondola_count} full: {current_ski_pairs_in_gondola} pairs of skis\n"
)

# Check if the last gondola had the most skis
if current_ski_pairs_in_gondola > max_ski_pairs:
    max_ski_pairs = current_ski_pairs_in_gondola
    gondola_with_max_skis = gondola_count

# Display final results
print(f"\nNumber of skiers: {num_skiers}")
print(f"Number of gondolas needed: {gondola_count}")
print(
    f"Gondola with the most skis: {gondola_with_max_skis} ({max_ski_pairs} pairs of skis)"
)
