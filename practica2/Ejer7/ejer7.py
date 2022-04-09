palabra =input('ingrese una palbra: ').lower().replace(' ','')
palabra =[letter for letter in palabra]
if(len(palabra) == len(set(palabra))):
    print('es heterograma')
else:
    print('no es heterograma')