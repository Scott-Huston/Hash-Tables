# '''
# Linked List hash table key/value pair
# '''

import hashlib

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
        self.stored = 0


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
        pass


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


        # code for automatic resizing
        # # if storage is full, resize hash table
        # if self.stored == self.capacity:
        #     self.resize()

        # if a value for this key already exists, delete it before adding new value
        if self.retrieve(key) != None:
            self.remove(key)
        
        # increment storage counter
        self.stored += 1

        # get index
        index = self._hash_mod(key)

        # check if index is already filled
        if self.storage[index] != None:
            # finding end node
            node = self.storage[index]
            while node.next is not None:
                node = node.next
            
            # adding LinkedPair to end of index list
            node.next = LinkedPair(key, value)

        # if not, add item to list
        else:
            self.storage[index] = LinkedPair(key, value)
            

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)

        try:
            node = self.storage[index]
            prev = None

            # finding right node to remove and nodes around it
            while node:
                next = node.next
                if node.key == key:
                    break
                prev = node
            
                node = node.next
            
            # removing node from list
            if prev:
                prev.next = next
            
            else:
                self.storage[index] = None

            self.stored -= 1
        
        except:
            print('index not found')


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''

        index = self._hash_mod(key)
        node = self.storage[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # doubling capacity
        self.capacity = self.capacity*2

        # saving existing storage and creating new blank storage
        old_storage = []

        for node in self.storage:
            while node:
                old_storage.append((node.key, node.value))
                node = node.next

        self.storage = [None]*self.capacity
        
        # adding each element from old storage to new storage
        self.stored = 0
        for pair in old_storage:
            self.insert(pair[0], pair[1])
        
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
