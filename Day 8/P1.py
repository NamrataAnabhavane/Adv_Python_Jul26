def squares(n):
    for i in range(1,n+1):
        yield i**2


sq = squares(5)
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
