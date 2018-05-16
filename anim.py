import numpy as np
from matplotlib import pyplot as plt
import matplotlib.patches as patches
import matplotlib.animation
import functions as fun
from math import *

def animation(agents, function, lb, ub):

    side = np.linspace(lb, ub, (ub - lb) * 5)
    X, Y = np.meshgrid(side, side)
    Z = np.array([np.array([function([X[i][j], Y[i][j]])
                            for j in range(len(X))])
                  for i in range(len(X[0]))])

    fig = plt.figure()
    plt.axes(xlim=(lb, ub), ylim=(lb, ub))
    plt.pcolormesh(X, Y, Z, shading='gouraud')
    plt.colorbar()

    x = np.array([j[0] for j in agents[0]])
    y = np.array([j[1] for j in agents[0]])
    sc = plt.scatter(x, y, color='black')

    plt.title(function.__name__, loc='left')

    def an(i):
        x = np.array([j[0] for j in agents[i]])
        y = np.array([j[1] for j in agents[i]])
        sc.set_offsets(list(zip(x, y)))
        plt.title('iteration: {}'.format(i), loc='right')

    ani = matplotlib.animation.FuncAnimation(fig, an, frames=len(agents) - 1)

    plt.show()


def animation_room(pos, function, lb, ub):

    mes = [0.7,0.2, 0.50,0.30, 0.25,0.25, 0.25,0.25, 0.70,0.40, 0.45,0.40, 0.30,0.20, 0.70,0.20, 0.20,0.20, 0.45,0.20]
    side = np.linspace(lb, ub, (ub - lb) * 5)
    fig = plt.figure()
    plt.axis('equal')
    ax = fig.add_subplot(111)
    ax.set_xlim(lb, ub)
    ax.set_ylim(lb, ub)
    tel = patches.Rectangle((pos[0][0]-0.5*mes[0], pos[0][1]-0.5*mes[1]), mes[0], mes[1], fill=False,edgecolor="red", hatch='+', label='tel')
    law = patches.Rectangle((pos[0][2] - 0.5 * mes[2], pos[0][3] - 0.5 * mes[3]), mes[2], mes[3], fill=False,edgecolor="green",hatch='+', label='law')
    puf1 = patches.Rectangle((pos[0][4] - 0.5 * mes[4], pos[0][5] - 0.5 * mes[5]), mes[4], mes[5], fill=False,edgecolor="green",hatch='o', label='puf1')
    puf2 = patches.Rectangle((pos[0][6] - 0.5 * mes[6], pos[0][7] - 0.5 * mes[7]), mes[6], mes[7], fill=False,edgecolor="green",hatch='x',label='puf2')
    kan = patches.Rectangle((pos[0][8] - 0.5 * mes[8], pos[0][9] - 0.5 * mes[9]), mes[8], mes[9], fill=False,edgecolor="red",hatch='o',label='kan')
    fot = patches.Rectangle((pos[0][10] - 0.5 * mes[10], pos[0][11] - 0.5 * mes[11]), mes[10], mes[11], fill=False,edgecolor="green",hatch='0',label='fot')
    sz1 = patches.Rectangle((pos[0][12] - 0.5 * mes[12], pos[0][13] - 0.5 * mes[13]), mes[12], mes[13], fill=False,edgecolor="red",hatch='x',label='sz1')
    sz2 = patches.Rectangle((pos[0][14] - 0.5 * mes[14], pos[0][15] - 0.5 * mes[15]), mes[14], mes[15], fill=False,edgecolor="red",hatch='0',label='sz2')
    sz3 = patches.Rectangle((pos[0][16] - 0.5 * mes[16], pos[0][17] - 0.5 * mes[17]), mes[16], mes[17], fill=False,edgecolor="red",hatch='.',label='sz3')
    sz4 = patches.Rectangle((pos[0][18] - 0.5 * mes[18], pos[0][19] - 0.5 * mes[19]), mes[18], mes[19], fill=False, edgecolor="red",hatch='*',label='sz4')
    r = sqrt(-fun.room(pos[0])/pi)
    carp = patches.Circle((2,2),radius=r, fill=False, edgecolor="blue")
    plt.plot([0, 0], [1.4, 2.6], 'b-', lw=3)
    plt.plot([2.55, 3.45], [0,0], 'g-', lw=3)
    plt.plot([2],[2])
    ax.add_patch(tel)
    ax.add_patch(law)
    ax.add_patch(puf1)
    ax.add_patch(puf2)
    ax.add_patch(kan)
    ax.add_patch(fot)
    ax.add_patch(sz1)
    ax.add_patch(sz2)
    ax.add_patch(sz3)
    ax.add_patch(sz4)
    ax.add_patch(carp)
    ax.legend()
    plt.title(function.__name__, loc='left')

    def an(i):
        tel.set_xy((pos[i][0] - 0.5 * mes[0], pos[i][1]-0.5*mes[1]))
        law.set_xy((pos[i][2] - 0.5 * mes[2], pos[i][3] - 0.5 * mes[3]))
        puf1.set_xy((pos[i][4] - 0.5 * mes[4], pos[i][5] - 0.5 * mes[5]))
        puf2.set_xy((pos[i][6] - 0.5 * mes[6], pos[i][7] - 0.5 * mes[7]))
        kan.set_xy((pos[i][8] - 0.5 * mes[8], pos[i][9] - 0.5 * mes[9]))
        fot.set_xy((pos[i][10] - 0.5 * mes[10], pos[i][11] - 0.5 * mes[11]))
        sz1.set_xy((pos[i][12] - 0.5 * mes[12], pos[i][13] - 0.5 * mes[13]))
        sz2.set_xy((pos[i][14] - 0.5 * mes[14], pos[i][15] - 0.5 * mes[15]))
        sz3.set_xy((pos[i][16] - 0.5 * mes[16], pos[i][17] - 0.5 * mes[17]))
        sz4.set_xy((pos[i][18] - 0.5 * mes[18], pos[i][19] - 0.5 * mes[19]))
        carp.set_radius(sqrt(-fun.room(pos[i])/pi))
        plt.title('iteration: {}'.format(i), loc='right')

    ani = matplotlib.animation.FuncAnimation(fig, an, frames=len(pos) - 1, interval=500)

    plt.show()

