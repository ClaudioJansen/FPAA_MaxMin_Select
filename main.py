def maxmin_select(arr, left, right):
    """
    Função recursiva que retorna uma tupla (mínimo, máximo)
    para o subvetor arr[left:right+1] utilizando a técnica de divisão e conquista.
    """
    if left == right:
        return arr[left], arr[left]
    elif right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    else:
        mid = (left + right) // 2
        min1, max1 = maxmin_select(arr, left, mid)
        min2, max2 = maxmin_select(arr, mid + 1, right)
        overall_min = min(min1, min2)
        overall_max = max(max1, max2)
        return overall_min, overall_max


if __name__ == '__main__':
    numeros = [3, 1, 5, 9, 2, 6, 8, 4, 7]
    minimo, maximo = maxmin_select(numeros, 0, len(numeros) - 1)
    print("Minimo:", minimo)
    print("Maximo:", maximo)