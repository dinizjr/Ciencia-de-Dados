'''Crie uma função que receba uma string e retorne essa mesma string invertida. (Fazer o algoritmo sem auxilio de listas)'''

def reverseString(text):
    minuscula = text.lower()
    return ''.join(reversed(minuscula))
print(reverseString("cadeira"))
