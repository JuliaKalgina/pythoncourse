import matplotlib.pyplot as mt
import numpy as np
import random

#1

mt.plot([1, 2, 3, 4, 5], [10, 3, 11, 4, 10])
mt.ylabel('Some numbers')
mt.show()

#2

mt.plot([1, 2, 3], [1, 2, 3], '<g')
mt.show()

#3

r = np.array(random.sample(range(1, 100), 10))
mt.plot(r, r+3, 'b', r, r*8, 'k')
mt.show()

#4

mt.plot([1,4,5,8], [2,5,3,9])
mt.xlabel('Time')
mt.ylabel('My confidence')
mt.title('Me')
mt.show()

#5

ax = mt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = mt.plot(t, s, lw=2)

mt.annotate('local min', xy=(1.5, -1), xytext=(2.5, -1.5), arrowprops=dict(facecolor='green', shrink=0.05))
mt.ylim(-2, 2)
mt.show()

#6

t = np.arange(2., 20., 1.)
mt.plot(t, np.sqrt(t), 'r')
mt.annotate('Young', xy=(5, 2), xytext=(7.5, 1.8), arrowprops=dict(facecolor='blue', shrink=0.04))
mt.annotate('Old', xy=(18.5, 4), xytext=(17, 3), arrowprops=dict(facecolor='green', shrink=0.04))
mt.xlabel('Time')
mt.ylabel('Happiness')
mt.title('Unrealistic mental state')
mt.show()

#7

q = np.arange(0., 3., 1)
w = np.exp(q)
mt.plot(q, q**3, w, 'b')
mt.xlabel('Time')
mt.ylabel('My friend and I getting good at playing guitar')
mt.title('Dynamics')
mt.show()