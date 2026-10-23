def tr(a,b,c):
    if pow(a,2) + pow(b,2) == pow(c,2):
         return 'É um triângulo retângulo'
    elif pow(a, 2) + pow(c, 2) == pow(b, 2):
         return 'É um triângulo retângulo'
    elif pow(b, 2) + pow(c, 2) == pow(a, 2):
         return 'É um triângulo retângulo'
    else:
         return 'Não é um triângulo retângulo'

print(tr(10,6,8))



