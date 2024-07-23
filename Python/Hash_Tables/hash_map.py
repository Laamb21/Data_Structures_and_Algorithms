#Hash Map implementation

#Hash Map class
class HashMap:
    #Initialization
    def __init__(self, size = 100):
        self.size = size
        self.buckets = [[] for _ in range(size)] #A list of buckets, each elements is a list(handles collision)
        
    #Hash function: sum only the numerical values of the key, ignoring non-numeric characters
    def hash_function(self, key):
        numeric_sum = sum(int(char) for char in key if char.isdigit())
        return numeric_sum % 10
    
    #Put function
    def put(self, key, value):
        idx = self.hash_function(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value) #Update existing key
                return
        bucket.append((key, value))

    #Get function
    def get(self, key):
        idx = self.hash_function(key)
        bucket = self.buckets[idx]
        for k, v in bucket:
            if k == key:
                return v
        return None #Key not found
    
    #Remove function
    def remove(self, key):
        idx = self.hash_function(key)
        bucket = self.buckets[idx]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return
            
    #Print function
    def print_map(self):
        print("Hash Map Contents:")
        for i, bucket in enumerate(self.buckets):
            print(f"Bucket {i}: {bucket}")


#Creating Hash Map
hash_map = HashMap(size = 10)

#Adding elements to Hash Map
hash_map.put("123-456", "Liam")
hash_map.put("123-457", 'Abbi')
hash_map.put("123-458", "Will")
hash_map.put("123-459", "Sherry")
hash_map.put("123-467", "Claire")
hash_map.put("123-468", "Marcus")
hash_map.put("123-469", "Cristian")
hash_map.put("123-478", "Brandon")
hash_map.put("123-898", "Bri")

#Print Hash Map
hash_map.print_map()

#Get method call
print("\nName associated with '123-456':",hash_map.get("123-456"))

#Remove method call 
print("\nRemoving name for '123-898'")
hash_map.remove("123-898")


