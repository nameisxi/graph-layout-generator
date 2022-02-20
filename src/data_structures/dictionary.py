

class Dictionary():
    def __init__(self, object):
        self.size = len(object.keys())

    def _check_hash_collision(self):
        pass

    def add(self, key, value):
        # Map the key into a hash value 
        # and then map the hash value into the range of the dictionary array
        mask = self.size - 1
        index = hash(key) & mask

        pass
