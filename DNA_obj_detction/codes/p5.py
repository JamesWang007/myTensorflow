'''
    plot 3D data : scattering


'''

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = []
y = []
z = []

with open("../statistics/3features.txt", 'r') as file:
    for line in file:
        v_list = [x.strip() for x in line.split(' ')]
        v_list = list(filter(lambda v : v != '', v_list))
        #for v in v_list:
        #    print(v)
        x.append(float(v_list[0]))
        y.append(float(v_list[1]))
        z.append(float(v_list[2]))


ax.scatter(x, y, z, c='r', marker='o')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()