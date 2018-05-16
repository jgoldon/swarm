import functions as fun
import algorithms as algor
import anim
# alh = algor.ba(50, fun.ackley, -10, 10, 20, 20,
#                r0=0.9, V0=0.5, fmin=0, fmax=0.02, alpha=0.9, csi=0.9)
alh = algor.ba(50, fun.room, 0, 4, 20, 50,
                r0=0.9, V0=0.5, fmin=0, fmax=0.02, alpha=0.9, csi=0.9)

# anim.animation(alh.get_agents(), fun.ackley, -10, 10)
anim.animation_room(alh.get_agents()[0],fun.room,0, 4)
# print(fun.room())
# anim.animation3D(alh.get_agents(), fun.ackley, 10, -10)
# print(alh.get_agents())
# print(alh.get_Gbest())
