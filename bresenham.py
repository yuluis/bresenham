import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = 6, 6



def bres(p1, p2):
    # assert `x1` < `x2` and `y1` < `y2` and f(x) satisfies p1,p2

    x1, y1 = p1
    x2, y2 = p2

    cells = []

    # scale y by 1000 to increase integer division precision
    m = (1000 * y2 - 1000 * y1) // (x2 - x1)  # slope scaled by 1000, integer divide
    print("slope * 1000 = ", m)
    sline_val = 1000 * y1 # sline_val is value of f(x)
    i = x1
    j = y1

    while i < x2:
        cells.append([i, j])
        if sline_val + m > 1000 * (j + 1):
            j += 1
        else:
            sline_val += m
            i += 1

    return np.array(cells)

p1 = (0, 0)
p2 = (7, 5)

cells = bres(p1, p2)
print (cells)

plt.plot([p1[0], p2[0]], [p1[1], p2[1]])

for q in cells:
    plt.plot([q[0], q[0]+1], [q[1], q[1]], 'k')
    plt.plot([q[0], q[0]+1], [q[1]+1, q[1]+1], 'k')
    plt.plot([q[0], q[0]], [q[1],q[1]+1], 'k')
    plt.plot([q[0]+1, q[0]+1], [q[1], q[1]+1], 'k')

plt.grid()
plt.axis('equal')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Integer based Bresenham algorithm")

plt.show()