'''def to_upper(words):
    uppers = []
    for word in words:
        uppers.append(word.upper())
    return uppers

list_words = ('ciencia' , 'de', 'dados', 'facens')
print(to_upper((list_words)))

print(list(map(lambda w: w.upper(), list_words))'''
#**********
'''def odd(n):
    return true if n % 2 == 1 else false

def even(n):
    return true if n % 2 == 0 else false

numbers = list(range(11))
print(numbers)

odds = list(filter(odd, numbers))

print(odds)'''
#**********

'''numbers = list(range(11))
print(list(filter(lambda x: x % 2 == 1, numbers)))
print(list(filter(lambda x: x % 2 == 0, numbers)))'''

#filter,lambda
numbers = list(range(11))
print(numbers)

odd = list(filter(lambda x: x % 2 == 1, numbers))
even = list(filter(lambda x: x % 2 == 0, numbers))
print(odd)
print(even)

print(list(zip(odd, even)))

#list comprehension
'''numbers = list(range(11))
print(numbers)

odd = [x for x in numbers if x % 2 != 0]#retorno iteração e condição
even = [x for x in numbers if x % 2 == 0]
print(odd)
print(even)'''

#print(list(zip(odd, even)))
#generators
'''def q(i):
    if(i==0):
        return 0 + 1
print(q(0))'''

'''def generator():
    numbers = range(10)
    for i in numbers:
        yield i * i  #para cada for o yield volta e retorna o resultado


gen = generator()
for i in gen:
    print(i)'''

#Genarators Expression

'''def generator(numbers):
    for i in numbers:
        yield i * i #para cada for o yield volta e retorna o resultado


numbers = range(10)
for i in generator(numbers):
    print(i)'''

'''numbers = range(10)

gen = [n * n for n in numbers]#list comprehension
print(gen)

gen = (n * n for n in numbers)#generator
for n in gen:
    print(n)'''








