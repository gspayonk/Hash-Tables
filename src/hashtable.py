# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        # hash = 123
        # for x in key:
        #     hash = ((hash<<5)+ hash) + ord(x)
        # return hash


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        waterpuppies = self._hash_mod(key)
        #storing the value with given key
        node = self.storage[waterpuppies]

        if node is None or node.key == key:
            self.storage[waterpuppies] = LinkedPair(key,value)
        else:
            while True:
                if node.next is None or node.key == key:
                    node.next = LinkedPair(key,value)
                    break
            node = node.next



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        waterpuppies = self._hash_mod(key)
        node = self.storage[waterpuppies]
        prev = None

        while node.next is not None and node.key != key:
            prev = node
            node = node.next
        if prev is None:
            self.storage[waterpuppies] = node.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        waterpuppies = self._hash_mod(key)
        if self.storage[waterpuppies] is not None:
            if self.storage[waterpuppies].key == key:
                return self.storage[waterpuppies].value
            else:
                next_node = self.storage[waterpuppies].next
                while next_node is not None:
                    if next_node.key == key:
                        return next_node.value
                    else:
                        next_node = next_node.next
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.capacity *= 2
        previous_size = self.storage
        self.storage = [None] * self.capacity
        for p in previous_size:
            node = p
            while node is not None:
                self.insert(node.key, node.value)
                node = node.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
