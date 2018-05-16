import swarm
import numpy as np
from math import exp
from random import randint, uniform, random

class ba(swarm.sw):

    def __init__(self, n, function, lb, ub, dimension, iteration, r0=0.9,
                 V0=0.5, fmin=0, fmax=0.02, alpha=0.9, csi=0.9):

        super(ba, self).__init__()

        r = [r0 for i in range(n)]

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)

        velocity = np.zeros((n, dimension))
        V = [V0 for i in range(n)]

        Pbest = self.__agents[np.array([function(i)
                                        for i in self.__agents]).argmin()]
        Gbest = Pbest

        f = fmin + (fmin - fmax)

        for t in range(iteration):

            sol = self.__agents

            F = f * np.random.random((n, dimension))
            velocity += (self.__agents - Gbest) * F
            sol += velocity

            for i in range(n):
                if random() > r[i]:
                    sol[i] = Gbest + np.random.uniform(-1, 1, (
                        1, dimension)) * sum(V) / n

            for i in range(n):
                if function(sol[i]) < function(self.__agents[i]) \
                        and random() < V[i]:
                    self.__agents[i] = sol[i]
                    V[i] *= alpha
                    r[i] *= (1 - exp(-csi * t))

            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            Pbest = self.__agents[
                np.array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)

class aba(swarm.sw):

    def __init__(self, n, function, lb, ub, dimension, iteration):
        super(aba, self).__init__()

        self.__function = function

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)

        Pbest = self.__agents[np.array([function(x)
                                        for x in self.__agents]).argmin()]
        Gbest = Pbest

        if n <= 10:
            count = n - n // 2, 1, 1, 1
        else:
            a = n // 10
            b = 5
            c = (n - a * b - a) // 2
            d = 2
            count = a, b, c, d

        for t in range(iteration):

            fitness = [function(x) for x in self.__agents]
            sort_fitness = [function(x) for x in self.__agents]
            sort_fitness.sort()

            best = [self.__agents[i] for i in
                    [fitness.index(x) for x in sort_fitness[:count[0]]]]
            selected = [self.__agents[i]
                        for i in [fitness.index(x)
                                  for x in sort_fitness[count[0]:count[2]]]]

            newbee = self.__new(best, count[1], lb, ub) + self.__new(selected,
                                                                   count[3],
                                                                   lb, ub)
            m = len(newbee)
            self.__agents = newbee + list(np.random.uniform(lb, ub, (n - m,
                                                                   dimension)))

            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            Pbest = self.__agents[
                np.array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)

    def __new(self, l, c, lb, ub):

        bee = []
        for i in l:
            new = [self.__neighbor(i, lb, ub) for k in range(c)]
            bee += new
        bee += l

        return bee

    def __neighbor(self, who, lb, ub):

        neighbor = np.array(who) + uniform(-1, 1) * (
            np.array(who) - np.array(
                self.__agents[randint(0, len(self.__agents) - 1)]))
        neighbor = np.clip(neighbor, lb, ub)

        return list(neighbor)


class fa(swarm.sw):

    def __init__(self, n, function, lb, ub, dimension, iteration, csi=1, psi=1,
                 alpha0=1, alpha1=0.1, norm0=0, norm1=0.1):

        super(fa, self).__init__()

        self.__agents = np.random.uniform(lb, ub, (n, dimension))
        self._points(self.__agents)

        Pbest = self.__agents[np.array([function(x)
                                        for x in self.__agents]).argmin()]
        Gbest = Pbest

        for t in range(iteration):

            alpha = alpha1 + (alpha0 - alpha1) * exp(-t)

            for i in range(n):
                fitness = [function(x) for x in self.__agents]
                for j in range(n):
                    if fitness[i] > fitness[j]:
                        self.__move(i, j, t, csi, psi, alpha, dimension,
                                    norm0, norm1)
                    else:
                        self.__agents[i] += np.random.normal(norm0, norm1,
                                                             dimension)

            self.__agents = np.clip(self.__agents, lb, ub)
            self._points(self.__agents)

            Pbest = self.__agents[
                np.array([function(x) for x in self.__agents]).argmin()]
            if function(Pbest) < function(Gbest):
                Gbest = Pbest

        self._set_Gbest(Gbest)

    def __move(self, i, j, t, csi, psi, alpha, dimension, norm0, norm1):

        r = np.linalg.norm(self.__agents[i] - self.__agents[j])
        beta = csi / (1 + psi * r ** 2)

        self.__agents[i] = self.__agents[j] + beta * (
            self.__agents[i] - self.__agents[j]) + alpha * exp(-t) * \
                                                   np.random.normal(norm0,
                                                                    norm1,
                                                                    dimension)