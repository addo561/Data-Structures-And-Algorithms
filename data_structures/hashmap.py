class HashMap:
    def __init__(self, size=100):
        self.size = size
        self.buckets = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def set(self, key, value):
        index = self._hash_function(key)
        for kvp in self.buckets[index]:
            if kvp[0] == key:
                kvp[1] = value  # Update value if key already exists
                return
        self.buckets[index].append([key, value])  # Add new key-value pair

    def get(self, key):
        index = self._hash_function(key)
        for kvp in self.buckets[index]:
            if kvp[0] == key:
                return kvp[1]  # Return value if key is found
        raise KeyError(f"Key '{key}' not found")

    def remove(self, key):
        index = self._hash_function(key)
        for i, kvp in enumerate(self.buckets[index]):
            if kvp[0] == key:
                del self.buckets[index][i]  # Remove key-value pair if key is found
                return
        raise KeyError(f"Key '{key}' not found")


# Example usage:
my_map = HashMap()
my_map.set("apple", 10)
my_map.set("banana", 20)
my_map.set("orange", 30)

print(my_map.get("apple"))  # Output: 10
print(my_map.get("banana"))  # Output: 20
print(my_map.get("orange"))  # Output: 30

my_map.remove("banana")
try:
    print(my_map.get("banana"))  # Raises KeyError
except KeyError as e:
    print(e)  # Output: Key 'banana' not found
