#Hash Set implementation

#Hash Set class
class HashSet:
    #Initialization
    def __init__(self, size = 100):
        self.size = size
        self.buckets = [[] for _ in range(size)] #List of buckets, each element is a list(handles collision)

    #Hash function: sum of character codes % number of buckets
    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size
    
    #Add function
    def add(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value not in bucket:
            bucket.append(value)

    #Contains function
    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        return value in bucket
    
    #Remove function
    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.buckets[index]
        if value in bucket:
            bucket.remove(value)

    #Print function
    def print_set(self):
        print("Hash Set contains:")
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")


#Create Hash Set
hash_set = HashSet(size = 10)

#Add elements to Hash Set
hash_set.add("Liam")
hash_set.add("Abbi")
hash_set.add("Will")
hash_set.add("Sherry")
hash_set.add("Claire")
hash_set.add("Marcus")
hash_set.add("Cristian")
hash_set.add("Brandon")

#Print Hash Set
hash_set.print_set()

#Contains method call
print("\n'Liam' is in the set:",hash_set.contains('Liam'))

#Remove method call
print("Removing 'Liam'")
hash_set.remove('Liam')
print("'Liam' is in the set:",hash_set.contains('Liam'))

#Hash code
print("\n'Abbi' has hash code:",hash_set.hash_function('Abbi'))