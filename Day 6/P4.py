class CountDown:
    def __init__(self,start):
        self.current = start
        self.start = start
    
    def __iter__(self):
        """Return the iterator object itself."""
        return self
    
    def __next__(self):
        if self.current <1:
            raise StopIteration
        
        value = self.current
        self.current -= 1
        return value
print("Countdown")
countdown = CountDown(5)
print(next(countdown))
print(next(countdown))
print(next(countdown))
print(next(countdown))
print(next(countdown))
