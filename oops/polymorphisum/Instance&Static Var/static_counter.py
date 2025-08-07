class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1  # Increment static counter for each instance
    
    @staticmethod
    def get():
        print(f"Total instances created: {Counter.count}")
        
        
a= Counter()
b= Counter()
c= Counter()

# Output: Total instances created: 3
Counter.get()