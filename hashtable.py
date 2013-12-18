

class HashTable(object):
    def __init__(self, buckets = 10):
        self.ht = tuple([] for i in xrange(buckets))
        self.buckets = buckets

    def hash(self, key):
        return key % self.buckets

    def add(self, key, value):
        bucket = self.ht[self.hash(key)]
        self.remove_from_bucket(bucket, key)
        self.add_to_bucket(bucket, key, value)

    def lookup(self, key):
        bucket = self.ht[self.hash(key)]
        return self.retrieve_from_bucket(bucket, key)

    def remove(self, key):
        bucket = self.ht[self.hash(key)]
        self.remove_from_bucket(bucket, key)

    @staticmethod
    def add_to_bucket(bucket, key, value):
        bucket.append((key, value))

    @staticmethod
    def retrieve_from_bucket(bucket, key):
        for element in bucket:
            if element[0] == key:
                return element[1]
        return None
        # alternately, raise KeyError("No such key '%d'" % key)

    @staticmethod
    def remove_from_bucket(bucket, key):
        for element in bucket:
            if element[0] == key:
                bucket.remove(element)
                return


if __name__ == '__main__':
    ht = HashTable()
    print ht.ht
    ht.add(0, 'zero')
    print ht.ht
    ht.add(10, 'ten-collision')
    print ht.ht
    ht.add(2, 'two')
    print ht.ht
    ht.remove(0)
    print ht.ht
    print ht.lookup(10)
    print ht.lookup(0)
