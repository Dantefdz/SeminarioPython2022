from collections import Counter

frase=input('ingrese la frase:')
palabra=input('ingrese la palabra')
print(Counter(frase.split())[palabra])

