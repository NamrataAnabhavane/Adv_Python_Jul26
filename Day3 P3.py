add_lambda = lambda a,b:a+b
print(add_lambda(10,50))

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x%2==0,numbers))
print(even_numbers)

squared = list(map(lambda x:x**2,numbers))
print(squared)

student = {
    'name':'Namrata',
    'age':20,
    'grade': lambda x: f"Grade: {x}%"
}
print(student['grade'](91))