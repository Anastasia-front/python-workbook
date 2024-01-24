# Key aspects: methods for working with random variables


"""random.randint(a, b): Obtain a random integer from a uniform distribution in the interval between a and b inclusive.

random.random(): Get a random number between 0.0 (inclusive) and 1.0 (not inclusive).

random.randrange(start, stop[, step]): Get a random number from a given range, 
with the option to specify a step between the values.

random.shuffle(x): Shuffle the order of elements in list x.

random.choice(seq): Choose a random element from the sequence seq (list or tuple).

random.choices(population, weights=None, cum_weights=None, k=1): 
population - a list sequence from which a selection should be made.
weights - an optional list that specifies the probabilities (weights)
 of each element in the population list. These weights determine how 
 likely a particular item is to be selected. The length of the weights 
 list must be equal to the length of the population list.
cum_weights is also an optional list of cumulative weights. If specified, 
the weights list is ignored. The cumulative weight of each element 
is defined as the sum of its weight plus the weights of all previous elements.
k: Number of elements to select. By default, k=1.

Generates a random sample with the ability to specify probabilities for each element and repetition in the sample.
random.sample(population, k): Obtain unique random elements from the population list of length k.

random.uniform(a, b): Obtain a random real number N such that a <= N <= b."""

import random

print("~" * 30)
# randint
random_int = random.randint(1, 1000)
print(f"random_int - {random_int}")

print("~" * 30)
# random
random_random = random.random()
print(f"random_random - {random_random}")
print("~" * 30)


# randrange
target = random.randrange(1, 11, 2)
print(f"target - {target}")
print("~" * 30)

# shuffle
cards = ["Ace", "King", "Queen", "Jack", "10", "9", "8", "7", "6"]
random.shuffle(cards)
print(f"Shuffled deck: {cards}")
print("~" * 30)

# choice
fruits = ["apple", "banana", "orange"]
print(f"choice - {random.choice(fruits)}")
print("~" * 30)

# choices
chosen_item = random.choices(fruits, k=1)
print(f"chosen_item - {chosen_item}")
print("~" * 30)

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(f"chosen_numbers - {chosen_numbers}")
print("~" * 30)

colors = ["red", "green", "blue"]
weights = [10, 1, 1]
chosen_color = random.choices(colors, weights, k=1)
print(f"chosen_color - {chosen_color}")
print("~" * 30)

# sample
participants = ["Anna", "Brandon", "Dru", "Eleanor", "Joseph"]
team = random.sample(participants, 4)
print(f"Team: {team}")
print("~" * 30)

# uniform
price = random.uniform(50, 100)
print(f"Random price: {price:.2f}")
print("~" * 30)

print("dir(random)")
print(dir(random))
print("~" * 30)
