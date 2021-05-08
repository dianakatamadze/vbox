from multiprocessing import Process, Manager
import numpy as np

def umn(A, B, i, j, q, mag_lt):
    global result
    res = A[i][q] * B[q][j]
    mag_lt.append(res)
    print(A[i][q], B[q][j])

def wr_m(name, m):
    with open(name, "wt") as file:
        for row in m:
            file.write(" ".join(str(i) for i in row) + "\n")

if __name__ == '__main__':
    print('начинается вычисление')

    M1 = np.random.randint(100, size=(3, 3))
    M2 = np.random.randint(100, size=(3, 3))

    wr_m("матрица1.txt", M1)
    wr_m("матрица2.txt", M2)

    m1 = [[int(token) for token in row.split()]  for row in open("матрица1.txt") if row.strip()]
    m2 = [[int(token) for token in row.split()]  for row in open("матрица2.txt") if row.strip()]

    mag = Manager().list()
    result = []
    
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for q in range(len(m1[0])):
                p1 = Process(target=umn, args=(m1, m2, i, j, q, mag))
                p1.start()
                p1.join()
                
    mag_s = [sum(mag[i: i + len(m1[0])]) for i in range(0, len(mag), len(m1[0]))]
    m1 = [mag_s[i: i + len(m1)] for i in range(0, len(mag_s), len(m1))]
    
    wr_m("результат.txt", m1)
    
    print('программа завершена, результаты в файле результат.txt')