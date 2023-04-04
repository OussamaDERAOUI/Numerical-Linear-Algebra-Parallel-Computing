from mpi4py import MPI
import math

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

N = 840
pi = 0.0

for i in range(rank, N, size):
    x = (i + 0.5) / N
    pi += 4.0 / (1.0 + x**2)

pi *= 1.0 / N

print("Process ", rank, " computed pi = ", pi)