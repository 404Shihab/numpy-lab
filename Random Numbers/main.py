import numpy as np

rng = np.random.default_rng()

print(rng.integers(1,7)) # (start, end) end is exclusive (1-6)
print(rng.integers(low=1, high=100))
print(rng.integers(low=1, high=50, size=3)) # [ 2 40 31]
print(rng.integers(low=1,high=100,size=(3,2)))  # [[26 37]
                                                # [ 1  2]
                                                # [49 46]]


rng_seed = np.random.default_rng(seed=1) # Using the same seed produces the same random numbers each time
print(rng_seed.integers(low=1,high=100,size=(3,2))) 

#-----------------------------------------


print(np.random.uniform()) # Generates a random float between 0 (inclusive) and 1 (exclusive)

print(np.random.uniform(low=-1, high=1, size=3)) # [-0.84069039  0.29543803 -0.95863109]
print(np.random.uniform(low=-1, high=10, size=3)) # [7.82041727 2.2733182  1.16492467]


np.random.seed(seed=1)
print(np.random.uniform(low=-1, high=10, size=(3,2)))

#--------------------------------------------

# ----------Shuffle an array------------

array=np.array([1,2,3,4,5,6])
rng.shuffle(array)
print(array)

#-------------------------------------------

fruits = np.array(['apple','banana','orange','coconut','pineapple'])

fruit = rng.choice(fruits)
print(fruit)

fruit = rng.choice(fruits,size=3)
print(fruit)

emojis = np.array(['😅','🙂','😃','🫠','😞'])
emoji =rng.choice(emojis,size=(2,3))
print(emoji)