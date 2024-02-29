class MagiaNumerica:
    def __init__(self, lista):
        self.lista = lista

    def eliminar_duplicados(self):
        lista_modificada = list(dict.fromkeys(self.lista))
        return lista_modificada

    def ordenar_mayor_menor(self):
        lista_modificada = list(set(self.lista))
        lista_modificada.sort(reverse=True)
        return lista_modificada

    def eliminar_impares(self):
        lista_modificada = list(set(self.lista))
        lista_modificada = [num for num in lista_modificada if num % 2 == 0]
        return lista_modificada

    def sumar_numeros(self):
        lista_modificada = list(set(self.lista))
        lista_modificada = [num for num in lista_modificada if num % 2 == 0]
        suma = sum(lista_modificada)
        return suma

    def colocar_suma_al_principio(self):
        lista_modificada = list(set(self.lista))
        lista_modificada = [num for num in lista_modificada if num % 2 == 0]
        suma = sum(lista_modificada)
        lista_modificada.insert(0, suma)
        return lista_modificada


def main():
    numeros = [1, 2, 3, 4, 4, 5, 6, 6, 7, 8, 9, 9, 10]
    magia = MagiaNumerica(numeros)

    print("Lista original:", numeros)

    resultado = magia.eliminar_duplicados()
    print("Lista después de eliminar duplicados:", resultado)

    resultado = magia.ordenar_mayor_menor()
    print("Lista después de ordenar de mayor a menor:", resultado)

    resultado = magia.eliminar_impares()
    print("Lista después de eliminar impares:", resultado)

    suma = magia.sumar_numeros()
    print("Suma de los números después de la magia numérica:", suma)

    resultado = magia.colocar_suma_al_principio()
    print("Lista después de colocar la suma al principio:", resultado)


if __name__ == "__main__":
    main()
