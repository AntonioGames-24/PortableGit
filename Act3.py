def recursive_bubble_sort(arr, start, end):
    if start >= end:
        return
    if arr[start] > arr[start + 1]:
        arr[start], arr[start + 1] = arr[start + 1], arr[start]
    recursive_bubble_sort(arr, start + 1, end)

def recursive_insertion_sort(arr, n):
    if n <= 1:
        return
    recursive_insertion_sort(arr, n - 1)
    last = arr[n - 1]
    j = n - 2
    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = last

def main():
    N = int(input("Ingresa el tamaño de tu arreglo: "))
    arr = []
    for i in range(N):
        num = int(input(f"Ingresa el numero en posicion {i + 1}: "))
        arr.append(num)
    
    choice = int(input("Elige el método de ordenamiento (1 para Bubble Sort, 2 para Inserción): "))
    
    if choice == 1:
        for i in range(1, N):
            recursive_bubble_sort(arr, 0, N - i)
        print("Tu arreglo ordenado por Bubble Sort es:")
    elif choice == 2:
        recursive_insertion_sort(arr, N)
        print("Tu arreglo ordenado por Inserción es:")
    else:
        print("Opción no válida.")
        return
    
    for num in arr:
        print(num, end=" ")

if __name__ == "__main__":
    main()
