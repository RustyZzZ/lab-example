# Вивести спочатку факторіали парних, а потім числа які не діляться на 3. Вивести суму чисел які не повторються парні.
import random
import math


def generate_array(N, min, max):
    random_array = []
    for i in range(N):
        random_array.append(random.randint(min, max))
    print(random_array)
    return random_array


def generate_2d_array(N, M, min, max):
    random_array = []
    for i in range(N):
        random_array.append(generate_array(M, min, max))
    return random_array


def pring2d(array2d):
    for array in array2d:
        print(array)


def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)


def task_1():
    # array = input("Enter array: ").split()

    # array = [int(x) for x in input().split()]
    result = []
    resultOdd = []
    evenElements = []
    for i in range(N):
        if i % 2 == 0:
            el = int(array[i])
            evenElements.append(el)
            result.append(fact(el))
        else:
            el = int(array[i])
            if (el % 3) != 0:
                resultOdd.append(el)
    suma = 0
    result += resultOdd
    for el in evenElements:
        count = evenElements.count(el)
        if count == 1:
            suma += el
    result.append(suma)
    print(result)


# 1.	Для кожного позитивного елементу масиву знайти, чи є в масиві елементи, рівні йому за модулем, але протилежні за знаком.
# Вивести індекси таких позитивних елементів масиву на екран для яких умова справджується.
def task_2(array):
    N = len(array)
    at_least_once = False
    for i in range(N):
        if array[i] > 0:
            for j in range(N):
                if array[i] == array[j] * (-1):
                    print(str(i))
                    at_least_once = True
                    break
    if not at_least_once:
        print("No results")


# 3.	Підрахувати кількість пар сусідніх елементів, які мають протилежні знаки.
# Просумувати індекси елементів масиву, що входять в ці пари.
# ПРИМІТКА. Вважати нуль позитивним числом.
def task_3(array):
    result = []
    for i in range(len(array) - 1):
        if (array[i] >= 0 > array[i + 1]) or (array[i] < 0 <= array[i + 1]):
            result.append(str(i + i + 1))
    print("result: " + str(result))
    print("count: " + str(len(result)))


# 5.	Елемент вектора називається локальним максимумом, якщо він строго більше двох своїх сусідів.
# Знайти всі локальні максимуми в межах масиву і вивести на екран номери  локальних  максимумів.
def task_5(array):
    for i in range(1, len(array) - 1):
        if array[i] > array[i - 1] and array[i] > array[i + 1]:
            print("Local Maximum: " + str(i))


# 7.	Вивести на екран індекси елементів масиву,
# які більші середнього значення всіх елементів масиву та індекси елементів масиву, які є степенями 4.
def task_7(array):
    sum = 0
    for i in array:
        sum += i
    average = (sum * 1.0) / len(array)

    for i in range(len(array)):
        if array[i] > average:
            print("GTA: " + str(i))
        log4 = math.log(array[i], 4)
        if round(log4) == log4:
            print("pow 4: ", i)


# 1.	Яка знаходить найбільше значення серед тих елементів стовпчиків,
# добуток елементів яких найбільший та знаходить найбільший елемент у тому рядку матриці,
# сума модулів елементів у яких найменша.
def task_2_1(array, N, M):
    min_row = 99999
    min_row_index = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += abs(array[i][j])
        if sum < min_row:
            min_row = sum
            min_row_index = i
    max = -999999
    for j in range(M):
        if array[min_row_index][j] > max:
            max = array[min_row_index][j]
    print(max)
    max_dob = -99999
    max_dob_index = 0
    for i in range(M):
        dob = 1
        for j in range(N):
            dob *= array[j][i]
        if dob > max_dob:
            max_dob = dob
            max_dob_index = i
    max = -999999
    for i in range(N):
        if array[i][max_dob_index] > max:
            max = array[i][max_dob_index]
    print(max)


if __name__ == '__main__':
    N = int(input("Enter n: "))
    M = int(input("Enter m: "))
    min = int(input("Enter min: "))
    max = int(input("Enter max: "))

    # array = generate_array(N, min, max)
    array = generate_2d_array(N, M, min, max)
    # task_2(array)
    # task_3(array)
    # task_5(array)
    # task_7(array)
    # task_2_1(array, N, M)
    # task_2_1(array, N, M)
