#Salwa Iqlima KVG
#NIM 2000680

import numpy as np

# Input jumlah data
n = int(input('Masukan jumlah data: '))

x = np.zeros((n))
y = np.zeros((n))


#Input nilai x dan y
print('Masukan nilai x dan y: ')
for i in range(n):
    x[i] = float(input( 'x['+str(i)+']='))
    y[i] = float(input( 'y['+str(i)+']='))


#Input titik interpolasi
xp = float(input('Masukan titik interpolasi: '))

yp = 0

#Implementasi polinom Lagrange
for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (xp - x[j])/(x[i] - x[j])
    yp = yp + p * y[i]    

#Hasil :
print('Nilai interpolasi di titik %.3f adalah %.3f.' % (xp, yp))