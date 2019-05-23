# Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
# The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

# Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.

#  NOTE: If you are using any global variables, make sure to clear them in the constructor. 
# Example :

# Input : 
#          capacity = 2
#          set(1, 10)
#          set(5, 12)
#          get(5)        returns 12
#          get(1)        returns 10
#          get(10)       returns -1
#          set(6, 14)    this pushes out key = 5 as LRU is full. 
#          get(5)        returns -1 

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.dic = {}
        self.queue = []
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key in self.dic:
            self.queue.pop(self.queue.index(key))
            self.queue.append(key)
            return self.dic[key]
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        n = len(self.dic)
        if key in self.dic:
            self.dic[key]=value
            self.queue.pop(self.queue.index(key))
            self.queue.append(key)
        else:
            if n>=self.capacity:
                key_to_delete = self.queue[0]
                del self.dic[key_to_delete]
                self.queue.pop(0)
            self.dic[key] = value
            self.queue.append(key)
                
# cache = LRUCache(2)
# cache.set(2,1)
# print(cache.dic,cache.queue)
# cache.set(1,1)
# print(cache.dic,cache.queue)
# cache.set(2,3)
# print(cache.dic,cache.queue)
# cache.set(4,1)
# print(cache.dic,cache.queue)
# print(cache.get(1))
# print(cache.dic,cache.queue)
# print(cache.get(2))

cache = LRUCache(1)
cache.set(2,1)
print(cache.dic,cache.queue)
print(cache.get(2))
print(cache.dic,cache.queue)
cache.set(3,2)
print(cache.dic,cache.queue)
print(cache.get(2))
print(cache.dic,cache.queue)
print(cache.get(3))
print(cache.dic,cache.queue)


