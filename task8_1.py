import numpy as np

#1
vec = np.zeros(10)
print('№1:', vec)

#2
vect = np.zeros(10)
vect[4] = 1
print('№2:', vect)

#3
v = np.full(10, 14.8)
print('№3:', v)

#4
vvv = np.arange(23, 39)
print('№4:', vvv)

#5
vv = np.arange(11)
vv = vv[::-1]
print('№5:', vv)

#6
vr = np.arange(9).reshape(3, 3)
print('№6:', vr)

#7
mm = np.arange(0, 9).reshape(3, 3)
print('№7:', mm)

#8
MyM = np.nonzero([1, 2, 0, 0, 4, 0])
print('№8:', MyM)

#9
M = np.random.random((10, 10))
print('№9:', M)
Vmin = M.min()
Vmax = M.max()
print(Vmin, Vmax)

#10
Vvector = np.random.random(15)
maximum = Vvector.argmax()
minimum = Vvector.argmin()
print('№10:', maximum, minimum)

#11
Vector = np.random.random(30)
average = Vector.mean()
print('№11:', average)

#12
rm = np.random.random((3, 10))
avstb = np.mean(rm, axis=0)
avstr = np.mean(rm, axis=1)
print('№12:', avstr, avstb)

#13
massiv = np.array([[1, 1, 1], [1, 1, 1]])
massiv1 = np.pad(massiv, pad_width=1, constant_values=0)
print('№13:', massiv1)

#14
x = np.dot(np.ones((5, 3)), np.ones((3, 2)))
print('№14:', x)

#15
M1 = np.array([[1, 2, 3], [1, 2, 1]])
M2 = np.array([[2, 3, 4], [5, 2, 1]])
commons = np.intersect1d(M1, M2)
print('№15:', commons)

#16
vEc = np.random.random(10)
print('№16:', vEc)
vEc1 = np.sort(vEc)
print(vEc1)

#17
Vector2 = np.random.random(10)
print('№17:', Vector2)
Vector2[Vector2.argmax()] = 0
print(Vector2)

#18

#1способ
ll = np.arange(0, 9).reshape(3, 3)
print('№18:', ll)
lll = ll.flatten()
print(lll)

#2способ
ww = np.arange(0, 9).reshape(3, 3)
qq = ww.reshape(1, 9)
print(qq)

#19
rmat = np.random.random((4, 4))
print('№19:', rmat)
rmat_max = rmat.max(keepdims=True)
print(rmat_max)
rmat1 = rmat - rmat_max
print(rmat1)

#20
mn = np.fromfile("textf.txt", sep=',', dtype=float)
mn1 = mn + 2
print('№20:', mn1)
