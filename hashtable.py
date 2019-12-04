#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)
    
    def get_bucket(self, key):
        """Uses the hash value of the specific key to return the corresponding bucket"""
        return self.buckets[self._bucket_index(key)]

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) It's necessary to loop through each bucket (b)
        and each item in each bucket (l) in order to access all of the keys in the hashtable,
        and b * l = n"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) Same as keys, except we're accessing values instead of keys."""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) because it has to get all the items in each bucket"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) because we loop through all buckets (b), then find all 
        key-value pairs in each bucket (l), and b * l = n."""
        count = 0
        # Loop through all buckets
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            for key, value in bucket.items():
                count += 1
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(1) best case when key is in the head node of the bucket.
                            O(l) worst case when key does not exist"""
        # Find bucket where given key belongs
        bucket = self.get_bucket(key)
        # Check if key-value entry exists in bucket
        for current_key, value in bucket.items():
            if current_key == key:
                return True
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(1) best case when key is in head node of bucket
                            O(l) worst case when key isn't in bucket"""
        # Find bucket where given key belongs
        bucket = self.get_bucket(key)
        # Check if key-value entry exists in bucket
        if self.contains(key):
            for current_key, value in bucket.items():
                # If found, return value associated with given key
                if current_key == key:
                    return value
        # Otherwise, raise error to tell user get failed
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) best case when key is in head node of bucket
                      O(l) worst case when key isn't in bucket"""
        # Find bucket where given key belongs
        bucket = self.get_bucket(key)
        # Check if key-value entry exists in bucket
        if self.contains(key):
            for current_key, current_value in bucket.items():
                # If found, update value associated with given key
                if current_key == key:
                    bucket.delete((current_key, current_value))
                    bucket.append((key, value))
        # Otherwise, insert given key-value entry into bucket
        else:
            bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(1) best case when key is in head node of bucket
                            O(l) worst case when key isn't in bucket"""
        # Find bucket where given key belongs
        bucket = self.get_bucket(key)
        # Check if key-value entry exists in bucket
        if self.contains(key):
            for current_key, value in bucket.items():
            # If found, delete entry associated with given key
                if current_key == key:
                    bucket.delete((current_key, value))
        # Otherwise, raise error to tell user delete failed
        else:
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()

    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
