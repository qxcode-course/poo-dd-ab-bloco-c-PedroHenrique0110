import random

class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self):
        return f'Foo({self.x})'
    
    def __repr__(self):
        return f'Foo({self.x})'

def main():
    #1 - Lista Vazia
    lista_vazia_int: list[int] = []
    lista_vazia: list[Foo] = []
    print(f"{lista_vazia_int} e {lista_vazia}")

    #2 - Lista Preenchida 
    lista_pree_int: list[int] = [1, 2, 3, 4, 5]
    lista_pree: list[Foo] = [Foo(1), Foo(2), Foo(3), Foo(4), Foo(5)]
    print(f"{lista_pree_int} e {lista_pree}")

    #3 - Append
    lista_pree_int.append(6)
    lista_pree.append(Foo(4))
    print(f"Depois do append {lista_pree_int}, {[str(f) for f in lista_pree]}")

    #4 - pop
    u_int = lista_pree_int.pop()
    u_list = lista_pree.pop()
    print(f"Depois do pop {lista_pree_int}, {[str(f) for f in lista_pree]} (removidos: {u_int} e {u_list})")

    #5 - Tamanho Lista
    print(f"Tamanho: {len(lista_pree_int)} e Tamanho 2: {len(lista_pree)}")

    #6 - Join
    print(f"Join: {', '.join(str(f) for f in lista_pree)}")

    #7 - Sequencia
    sequencia = list(range(11))
    print (f"Sequencia 0-10: {sequencia}")

    #8 - Numeros aleatorios
    aleatorio = [random.randint(1, 100) for _ in range (5)]
    print(f"Numeros Aleatórios: {aleatorio}")

    #9 - For range
    print("For Range:")
    for elemento in lista_pree_int:
        print(f"Elemento: {elemento}")

    #10 - For Indexado
    print("For Indexado:")
    for i in range (len(lista_pree_int)):
        print(f"Indice {i}: {lista_pree_int[i]}")

    #11 - Filtro
    par = [x for x in lista_pree_int if x % 2 == 0]
    print(f"Pares: {par}")

    #12 - Transformar Elementos no seu quadrado
    quadrado = [x ** 2 for x in lista_pree_int]
    print(f"Valores ao quadrado {quadrado}")


main()