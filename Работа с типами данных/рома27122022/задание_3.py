'''Дана матрица 5*5. Отсортируйте числа в каждой строке в порядке увеличения и верните новую матрицу.
Весь функционал должен лежать в функции.'''
matrix = [[5,10,8,6,1],
          [7,11,2,3,6],
          [12,0,3,11,5],
          [19,7,5,9,10],
          [1,21,0,12,3]]

def sort_matrix(matr):
    for i in matr:
        i.sort()
    print(matr)
    for i in matr:
        for elem in i:
            print(elem,end=' ')
        print()

sort_matrix(matrix)