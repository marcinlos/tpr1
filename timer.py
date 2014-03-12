from math import sqrt
from mpi4py import MPI

class Timer(object):
    def __init__(self):
        self.t_start = 0
        self.diff = 0

    def start(self):
        self.t_start = MPI.Wtime()

    def stop(self):
        t = MPI.Wtime()
        self.diff = t - self.t_start

    def printStats(self, n):
        avg = self.diff
        print('{0}'.format(1e3 * avg))
