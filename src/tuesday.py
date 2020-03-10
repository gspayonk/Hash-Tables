import random
​
def longest_linked_list_chain(keys, buckets, loops=10):
    """
    Roll keys number of keys into buckets number of random buckets
    and count collisions
​
    """
    for i in range(loops):
        key_counts = {}
        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1
        
        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]
​
        print(f"Longest Linked List Chain for {keys} keys in {buckets} buckets (Load Factor: {keys/buckets:.2f}): {largest_n}")
​
​
longest_linked_list_chain(500, 1000, 5)

import random
​
def how_many_before_collision(buckets, loops=1):
    """
    Roll random hashes indexes into buckets and print
    how many rolls before a collision
​
    Run loops times
    """
    for i in range(loops):
        tries = 0
        tried = set()
​
        tried_list = []
​
        while True:
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            if hash_index not in tried:
                tried.add(hash_index)
                tries += 1
​
            else:
                # We have found a collision
                break
​
        print(f"{buckets} buckets,  {tries} hashes before collision. ({tries/buckets * 100:.1f}%)")
​
​
how_many_before_collision(10000, 10)

