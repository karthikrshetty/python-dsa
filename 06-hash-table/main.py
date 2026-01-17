# ============================================================
# Hash Table Implementation (Separate Chaining)
# ============================================================

class HashTable:
    def __init__(self, size=7):
        """
        Initializes the hash table with a fixed number of buckets.

        Each bucket will either contain:
        - None
        - A list of [key, value] pairs (separate chaining)
        """
        self.data_map = [None] * size

    def __hash(self, key):
        """
        Hash function to convert a string key into a valid index.

        Hash Strategy:
        - Iterate over characters in the key
        - Multiply ASCII value by a constant
        - Apply modulo to keep index within bounds
        """
        my_hash = 0

        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)

        return my_hash

    def set_item(self, key, value):
        """
        Inserts a key-value pair into the hash table.

        Collision Handling:
        - Uses separate chaining (list at each index)
        """
        index = self.__hash(key)

        # Case 1: No bucket exists yet
        if self.data_map[index] is None:
            self.data_map[index] = []

        # Append key-value pair to the bucket
        self.data_map[index].append([key, value])

    def get_item(self, key):
        """
        Retrieves the value associated with a given key.

        Returns:
        - Value if key exists
        - None if key is not found
        """
        index = self.__hash(key)

        # Traverse bucket if it exists
        if self.data_map[index] is not None:
            for pair in self.data_map[index]:
                if pair[0] == key:
                    return pair[1]

        return None

    def keys(self):
        """
        Returns a list of all keys present in the hash table.
        """
        all_keys = []

        for bucket in self.data_map:
            if bucket is not None:
                for pair in bucket:
                    all_keys.append(pair[0])

        return all_keys

    def print_table(self):
        """
        Prints the internal structure of the hash table.
        Useful for debugging and visualization.
        """
        for index, bucket in enumerate(self.data_map):
            print(index, ":", bucket)


# ============================================================
# Hash Table Testing (Insertion, Retrieval, Structure)
# ============================================================

print("---- HASH TABLE INSERTION TEST ----")

my_hash_table = HashTable()

my_hash_table.set_item("bolts", 1400)
my_hash_table.set_item("washer", 1200)
my_hash_table.set_item("nuts", 1200)
my_hash_table.set_item("nails", 100)

print("\n---- HASH TABLE LOOKUP TEST ----")

print("bolts:", my_hash_table.get_item("bolts"))     # Expected: 1400
print("washer:", my_hash_table.get_item("washer"))   # Expected: 1200
print("lumber:", my_hash_table.get_item("lumber"))   # Expected: None

print("\n---- HASH TABLE KEYS ----")
print(my_hash_table.keys())

print("\n---- HASH TABLE STRUCTURE ----")
my_hash_table.print_table()
