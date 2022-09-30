#1.1
a=[]
def x(args):
    pass
for i in range(x):
    b=[]
    for j in range(x):
        print('Enter the element:')
        b.append(int(input()))
    a.append(b)
c = 0
d = 0
for i in range(x):
    for j in range(i + 1, x):
        if a[i][j] > 0:
            d += a[i][j]
            c+= 1
print("Number of positive: " , c)
print("Sum: " , d)

#1.2
x = 3
z = []
for i in range(x):
    z.append(list(map(int, input().split())))
def min_elts(z):
    return list(map(min, z))

#2.1
x=3
a=[]
for i in range(x):
    b=[]
    for j in range(x):
        print('Enter the element: ')
        b.append(int(input()))
    a.append(b)
def magic(a):
    x = 3
    z1 = 0
    z2 = 0
    for i in range(x):
        z1 += a[i][i]
        z2 += a[i][x - i - 1]
    if not (z1 == z2):
        return False
    for i in range(x):
        rows = 0
        cols = 0
        for j in range(x):
            rows  += a[i][j]
            cols += a[j][i]
        if not (rows  == cols == z1):
            return False
    return True
if (magic(a)):
    print("Magic Square")
else:
    print("Not a Magic Square")

#2.2
q=int(input('Enter the number of rows: '))
w=int(input('Enter the number of columns :'))
z=[]
for i in range(q):
    x=[]
    for j in range(q):
        print('Enter the element: ')
        x.append(int(input()))
    z.append(x)
print('Final array: ')
for i in range(w):
    for j in range(q):
        print(a[i][j], end=' ')
    print()
for i in range(q):
    temp = z[i][0]
    z[i][0] = z[i][w-1]
    z[i][w-1] = temp
for i in range(q):
    for j in range(w):
        print("%2d " % a[i][j], end=' ')
    print()

#3.1
z = int(input('z:'))
x = int(input('x:'))
q = []
for i in range(z):
    q.append(list(map(int, input().split())))
for i in range(x):
    for j in range(z):
        print(q[i][j], end=' ')
    print()
w = "YES"
for i in range(x):
    for j in range(z):
        if q[i][j] != q[j][i]:
            w = "NO"
            break
print(w)

#3.2
z=int(input('Enter the number of rows: '))
x=int(input('Enter the number of columns: '))
q=[]
for i in range(z):
    w=[]
    for j in range(z):
        print('Enter the elements: ')
        w.append(int(input()))
    q.append(w)
print('Final array: ')
for i in range(x):
    for j in range(z):
        print(q[i][j], end=' ')
    print()
max = q[0][0]
ie = je = 0
for i in range(x):
    for j in range(z):
        if q[i][j] > max:
            max = q[i][j]
            ie = i
            je = j
q[0], q[ie] = q[ie], q[0]
q[0][0], q[0][je] = q[0][je], q[0][0]
for row in q:
    print(*map('\{:2d\}'.format, row))

#4.1
z = int(input('n:'))
x = int(input('m:'))
a = []
for i in range(z):
    a.append(list(map(int, input().split())))
for i in range(x):
    for j in range(z):
        print(a[i][j], end=' ')
    print()
s = []
for i in range(len(a)):
    s.append(sum(a[i]))
print(a[s.index(max(s))], 'largest sum:', max(s), a[s.index(min(s))], 'smallest sum:', min(s))

#4.2
z = int(input('z:'))
x = int(input('x:'))
q = []
for i in range(z):
    q.append(list(map(int, input().split())))
for i in range(x):
    for j in range(z):
        print(a[i][j], end=' ')
    print()
q = [[1 if x > 0 else 0 for x in i] for i in q]
for i in range(len(q)):
    print(*[q[i][x] if x <= i else '' for x in range(len(q[i]))], '')

#5.1
def printArray(arr, x, z):
    for i in range(x):
        for j in range(z):
            print(arr[i][j], end=' ')
        print()
def sortArr(arr, x, z):
    for i in range(x):
        arr[i].sort()
    print()
z = int(input('Enter the number of rows: '))
x = int(input('Enter the number of columns: '))
a = []
for i in range(x):
    b = []
    for j in range(z):
        print('Enter the element: ')
        b.append(int(input()))
    a.append(b)
print('Final array: ')
printArray(a, x, z)
sortArr(a, x, z)
print('Changed array: ')
printArray(a, x, z)

#5.2
def smallestInRow(mat):
    minm = min(mat)
    return minm
n = int(input('n:'))
m = int(input('m:'))
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print()
minm = []
for i in range(n):
    minm.append(smallestInRow(a[i]))
print(minm)
for i in range(len(minm)):
    if minm[i] % 2 == 0:
        minm[i] = 0
    else:
        minm[i] = 1
print(minm)

#6.1
MAX = 100
def smallestInRow(mat, n, m):
    print("\{", end="")
    for i in range(n):
        min = mat[i][0]
        for j in range(1, m, 1):
            if (mat[i][j] < min):
                min = mat[i][j]
        print(min, end=",")
    print("\}")
def smallestInCol(mat, n, m):
    print("\{", end="")
    for i in range(m):
        min = mat[0][i]
        for j in range(1, n, 1):
            if mat[j][i] < min:
                min = mat[j][i]
        print(min, end=",")
    print("\}")
n = 3
m = 3
mat = [[2, 1, 7],
       [3, 7, 2],
       [5, 4, 9]]
print("Minimum element of each row is",
      end=" ")
smallestInRow(mat, n, m)
print("Minimum element of each column is",
          end=" ")
smallestInCol(mat, n, m)

#7.1
def lower(matrix, row, col):
    for i in range(0, row):
        for j in range(0, col)
            if i < j:
                print("0", end=" ")
            else:
                print(matrix[i][j],
                      end=" ")
        print(" ")
def upper(matrix, row, col):
    for i in range(0, row):
        for j in range(0, col):
            if i > j:
                print("0", end=" ")
            else:
                print(matrix[i][j],
                      end=" ")
        print(" ")
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
row = 3
col = 3
print("Lower triangular matrix: ")
lower(matrix, row, col)
print("Upper triangular matrix: ")
upper(matrix, row, col)

#7.2
def diagonal(A):
    N = 3
    for col in range(N):
        startcol = col
        startrow = 0
        while (startcol >= 0 and
               startrow < N):
            print(A[startrow][startcol], end=" ")
            startcol -= 1
            startrow += 1
        print()
    for row in range(1, N):
        startrow = row
        startcol = N - 1
        while (startrow < N and
               startcol >= 0):
            print(A[startrow][startcol],
                  end=" ")
            startcol -= 1
            startrow += 1
        print()
A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
diagonal(A)

#8.1
N = 4
def showMatrix(mat):
    i = None
    j = None
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=" ")
        print('')
def kthSmallest(arr, n, K):
    arr.sort()
    return arr[K - 1]
def ReplaceDiagonal(mat, K):
    i = None
    j = None
    arr = [0] * N
    for i in range(N):
        for j in range(N):
            arr[j] = mat[i][j]
        mat[i][i] = kthSmallest(arr, N, K)
    showMatrix(mat)
mat = [[1, 2, 3, 4], [4, 2, 7, 6], [3, 5, 1, 9], [2, 4, 6, 8]]
K = 3
ReplaceDiagonal(mat, K)

#9.1
MAX = 100
def largestSquare(matrix, R, C, q_i, q_j, K, Q):
    for q in range(Q):
        i = q_i[q]
        j = q_j[q]
        min_dist = min(min(i, j),
                       min(R - i - 1, C - j - 1))
        ans = -1
        for k in range(min_dist + 1):
            count = 0
            for row in range(i - k, i + k + 1):
                for col in range(j - k, j + k + 1):
                    count += matrix[row][col]
            if count > K:
                break
            ans = 2 * k + 1
        print(ans)
matrix = [[1, 0, 1, 0, 0],
          [1, 0, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 0, 0, 1, 0]]
K = 9
Q = 1
q_i = [1]
q_j = [2]
largestSquare(matrix, 4, 5, q_i, q_j, K, Q)

#9.2
def getcofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]
def determinantOfMatrix(mat):
    if len(mat) == 2:
        value = mat[0][0] * mat[1][1] - mat[1][0] * mat[0][1]
        return value
    Sum = 0
    for current_column in range(len(mat)):
        sign = (-1) ** current_column
        sub_det = determinantOfMatrix(getcofactor(mat, 0, current_column))
        Sum += (sign * mat[0][current_column] * sub_det)
    return Sum
mat = [[1, 0, 2, -1],
        [3, 0, 0, 5],
        [2, 1, 4, -3],
        [1, 0, 5, 0]]
print('Determinant of the matrix is :', determinantOfMatrix(mat))

#10.1
def maxelement(arr):
    no_of_rows = len(arr)
    no_of_column = len(arr[0])
    for i in range(no_of_rows):
        max1 = 0
        for j in range(no_of_column):
            if arr[i][j] > max1:
                max1 = arr[i][j]
        print(max1)
arr = [[3, 4, 1, 8],
       [1, 4, 9, 11],
       [76, 34, 21, 1],
       [2, 1, 4, 5]]
maxelement(arr)

#10.2
def sortRowWise(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            for k in range(len(m[i]) - j - 1):
                if m[i][k] > m[i][k + 1]:
                t = m[i][k]
                    m[i][k] = m[i][k + 1]
                    m[i][k + 1] = t
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()
m = [[9, 8, 7, 1], [7, 3, 0, 2], [9, 5, 3, 2], [6, 3, 1, 2]]
sortRowWise(m)

#11.1
n = int(input('Enter the size of the square matrix: '))
a = []
print('Enter your array: ')
for i in range(n):
    a.append([int(j) for j in input().split()])

min_ = [min(i) for i in a]
ind_row_with_min = min_.index(min(min_))

print('Min of array: ', min(map(min, a)))
print('Sum: ', format(sum(a[ind_row_with_min])))

#12.1
n = int(input('Enter the size of the square matrix: '))
a = []
print('Enter your array: ')
for i in range(n):
    a.append([int(j) for j in input().split()])
a_rev = list(map(list, zip(*a)))
for i in range(n):
    for j in range(n):
        if a[i] == a_rev[j]:
            print(i + 1, 'row and', j + 1, 'column are equal')

#12.2
def spec_subtract(matrix):
    for i in range(0, len(matrix) - 1):
        for j in range(0, len(matrix[i])):
            matrix[i][j] = matrix[i][j] - matrix[len(matrix) - 1][j]
    return matrix
z = int(input())
x = int(input())
c = []
for i in range(z):
    c.append(list(map(int, input().split())))
c = spec_subtract(matrix=c)
for i in range(z):
    for j in range(x):
        print(c[i][j], end=' ')
    print()

#13.2
z = int(input())
x = int(input())
c = []
for i in range(n):
    c.append(list(map(int, input().split())))
MIN = min(map(min, c))
MAX = max(map(max, c))
print('Min:', MIN, ', max:', MAX)
c[c.index(min(c))], c[c.index(max(c))] = c[c.index(max(c))], c[c.index(min(c))]
for i in range(z):
    for j in range(x):
        print(a[i][j], end=' ')
    print()