import random
def readInput(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        n = int(lines[0])
        arr = [int(line.strip()) for line in lines[1:]]
    return arr

def writeOutput(filename, x, y):
    with open(filename, 'w') as file:
        file.write(f"{x} {y}\n")

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



def main():
    inputFile = 'input_06_100.txt'
    outputFile = 'output_6.txt'
    original = readInput(inputFile)

    x = quickSortClassic(original.copy())
    y = quickSortMedian3(original.copy())
    writeOutput(outputFile, x, y)

if __name__ == '__main__':
    main()
