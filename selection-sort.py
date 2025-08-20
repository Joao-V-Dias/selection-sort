import data
import time

def selectionSort(lst):
    n = len(lst)
    start_time = time.perf_counter()
    cont = 0
    vtTest = []
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if lst[j] < lst[minIndex]:
                minIndex = j
            cont += 1
        lst[i], lst[minIndex] = lst[minIndex], lst[i]
        vtTest.append(lst[i])
        print(f"{vtTest}  |  {lst[i + 1:]}")

    execution_time = time.perf_counter() - start_time
    print(f"-> Tempo: {execution_time:.5f} segundos")
    print(f"-> Quantidade de iteracoes: {cont}")
    return lst

for i in range(len(data.lstInput)):
    lst = data.lstInput[i]
    print(f"-> Lista {i + 1}: {lst}")
    lst = selectionSort(lst)
    print(f"-> Lista {i + 1} ordenada: {lst}\n\n")


