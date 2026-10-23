def fibo(n):
    if n > 1:
        return fibo(n - 1) + fibo(n - 2)
    else:
        return n#no final da recursão tem que retornar valor fixo

print(fibo(10))



fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)

print(list(map(fibo, range(20))))
print(list(map(fib, range(20))))


