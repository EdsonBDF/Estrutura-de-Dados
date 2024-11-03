def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivô = arr[len(arr) // 2]
        menores = [x for x in arr if x < pivô]
        iguais = [x for x in arr if x == pivô]
        maiores = [x for x in arr if x > pivô]
        return quick_sort(menores) + iguais + quick_sort(maiores)

# Exemplo de uso:
arr = [7, 2, 9, 3, 6, 4, 5, 8, 1, 0]
print("Lista original:", arr)
print("Lista ordenada:", quick_sort(arr))