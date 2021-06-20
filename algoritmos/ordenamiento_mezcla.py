import random

def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2 
        izquierda = lista[:medio]
        derecha = lista[medio:]
        print(f'{izquierda}*****{derecha}')

        # Llamada recursiva en cada mitad
        ordenamiento_mezcla(izquierda)
        ordenamiento_mezcla(derecha)

        # Iteradotes para recorrer las dos sublistas
        i = 0
        j = 0
        # Iterador para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1

            k =+ 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            i += 1
            k += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            j += 1
            k += 1

        print(f'izquierda {izquierda}, derecha {derecha}')
        print(lista)
        print('-' * 50)

    return lista

if __name__ == '__main__':
    
    size_list = int(input('¿De qué tamaño será la lista?: '))

    lista = [random.randint(0,100) for i in range(size_list)]
    print(lista)
    print('-' * 2)

    lista_ordenada = ordenamiento_mezcla(lista)
    print(lista_ordenada)