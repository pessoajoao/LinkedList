from arrayListS import ArrayList, No

inicio = ArrayList()
impar = ArrayList()
par = ArrayList()

inicio.add(1)
inicio.add(2)
inicio.add(6)
inicio.add(7)
inicio.add(8)

proximo = inicio.header
while proximo is not None:
    if(proximo.carga%2 == 0):
        par.add(proximo)
    else: 
        impar.add(proximo)

    proximo = proximo.prox




impar.printList()
print()
par.printList()