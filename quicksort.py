import random
import sys
import matplotlib.pyplot as plt
import numpy as np

def readInput(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        arr = [int(line.strip()) for line in lines[1:]]
    return arr

def writeOutput(filename, x, y, z):
    with open(filename, 'w') as file:
        file.write(f"{x} {y} {z}\n")

# Класичний QuickSort з останнім елементом як pivot
def quickSortClassic(arr):
    comparisons = [0]

    def partition(p, r):
        x = arr[r]
        i = p - 1
        for j in range(p, r):
            comparisons[0] += 1
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    def quickSort(p, r):
        if p < r:
            q = partition(p, r)
            quickSort(p, q - 1)
            quickSort(q + 1, r)

    quickSort(0, len(arr) - 1)
    return comparisons[0]

# QuickSort з медіаною трьох
def quickSortMedian3(arr):
    comparisons = [0]

    def medianOfThree(p, q, r):
        a = arr[p]
        b = arr[(p + r) // 2]
        c = arr[r]
        triple = [(a, p), (b, (p + r) // 2), (c, r)]
        triple.sort(key=lambda x: x[0])
        return triple[1][1]

    def insertionSort(p, r):
        for i in range(p + 1, r + 1):
            key = arr[i]
            j = i - 1
            while j >= p:
                comparisons[0] += 1
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    j -= 1
                else:
                    break
            arr[j + 1] = key

    def partition(p, r):
        x = arr[r]
        i = p - 1
        for j in range(p, r):
            comparisons[0] += 1
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        return i + 1

    def quickSort(p, r):
        if r - p + 1 <= 3:
            insertionSort(p, r)
        elif p < r:
            m = medianOfThree(p, (p + r) // 2, r)
            arr[m], arr[r] = arr[r], arr[m]
            q = partition(p, r)
            quickSort(p, q - 1)
            quickSort(q + 1, r)

    quickSort(0, len(arr) - 1)
    return comparisons[0]

# 3rd alg
def sort_small(arr, p, r, comp):
    n = r - p + 1
    if n == 2:
        comp += 1  # порівняння arr[p] і arr[r]
        if arr[p] > arr[r]:
            arr[p], arr[r] = arr[r], arr[p]
        return comp
    elif n == 3:
        comp += 1  # порівняння arr[p] і arr[p+1]
        if arr[p] > arr[p+1]:
            arr[p], arr[p+1] = arr[p+1], arr[p]
        comp += 1  # порівняння arr[p+1] і arr[r]
        if arr[p+1] > arr[r]:
            arr[p+1], arr[r] = arr[r], arr[p+1]
        comp += 1  # повторне порівняння arr[p] і arr[p+1]
        if arr[p] > arr[p+1]:
            arr[p], arr[p+1] = arr[p+1], arr[p]
        return comp
    return comp

def partition(arr, p, r, comp):
    # Вибір трьох опорних елементів з A[p], A[p+1] та A[r]
    # Їх впорядкування не враховуємо (як зазначено)
    q1, q2, q3 = sorted([arr[p], arr[p+1], arr[r]])
    # Записуємо впорядковані опори назад:
    arr[p], arr[p+1], arr[r] = q1, q2, q3

    # Розбиття підмасиву з p+2 по r-1
    i = p + 2
    j = p + 2
    k = r - 1
    while i <= k:
        # Спочатку виконуємо порівняння з q1
        comp += 1
        if arr[i] < q1:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        else:
            # Якщо не менше за q1, виконуємо порівняння з q3
            comp += 1
            if arr[i] > q3:
                arr[i], arr[k] = arr[k], arr[i]
                k -= 1
                continue  # не збільшуємо i, щоб знову перевірити прийшовший елемент
        i += 1
    comp += 1  # додаємо операцію після завершення циклу

    # Переміщуємо опорні елементи у свої остаточні позиції:
    j -= 1  # позиція для q1
    k += 1  # позиція для q3
    arr[p], arr[j] = arr[j], arr[p]         # переміщуємо q1
    arr[p+1], arr[k] = arr[k], arr[p+1]       # переміщуємо q2 (середній опір)
    # q3 вже знаходиться у позиції r, його більше не переставляємо

    # Повертаємо позиції опорів (q1 знаходиться в j, q2 в k)
    return j, k, comp

def three_pivot_qs(arr, p, r, comp):
    if r - p + 1 <= 3:
        comp = sort_small(arr, p, r, comp)
        return comp
    # Розбиття:
    j, k, comp = partition(arr, p, r, comp)
    # Рекурсивно сортуємо три частини:
    comp = three_pivot_qs(arr, p, j - 1, comp)
    comp = three_pivot_qs(arr, j + 1, k - 1, comp)
    comp = three_pivot_qs(arr, k + 1, r, comp)
    return comp

def quick_sort_with_three_pivots(arr):
    comp = 0
    comp = three_pivot_qs(arr, 0, len(arr) - 1, comp)
    return comp
#generation
def generate_random_array(size):
    array = []
    for i in range(size):
        array.append(random.randint(1, 10000000))
    return array
def generate_sorted_array(size):
    return list(range(size))

def generate_reversed_sorted_array(size):
    return list(range(size - 1, -1, -1))

#graphs
size_of_array = [10, 100, 500]
y_classic = []
y_median = []
y_pivot = []
x_classic = []
x_median = []
x_pivot = []
def get_data(generate_function):
    y_classic.clear()
    y_median.clear()
    y_pivot.clear()
    x_classic.clear()
    x_median.clear()
    x_pivot.clear()
    for i in range(len(size_of_array)):
        generated_array = generate_function(size_of_array[i])
        x_classic.append(size_of_array[i])
        y_classic.append(quickSortClassic(generated_array))

        x_median.append(size_of_array[i])
        y_median.append(quickSortMedian3(generated_array))

        x_pivot.append(size_of_array[i])
        y_pivot.append(quick_sort_with_three_pivots(generated_array))

get_data(generate_random_array)
plt.title("Random arrays")
plt.plot(np.array(x_classic), np.array(y_classic), color="green")
plt.plot(np.array(x_median), np.array(y_median), color="red")
plt.plot(np.array(x_pivot), np.array(y_pivot), color="blue")
plt.legend()
plt.show()

def main():
    print("program")
    # inputFile = sys.argv[1]
    # outputFile = inputFile.replace(".txt", "_output.txt")
    # original = readInput(inputFile)
    # x = quickSortClassic(original.copy())
    # y = quickSortMedian3(original.copy())
    # z = quick_sort_with_three_pivots(original.copy())
    # writeOutput(outputFile, x, y, z)
    # print(f"Output written to {outputFile}")
if __name__ == '__main__':
    main()
