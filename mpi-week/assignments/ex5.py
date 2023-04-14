from mpi4py import MPI
import numpy as np
import time

# Matrix-vector multiplication function
def matrix_vector_mult(A, x):
    m = A.shape[0]
    n = A.shape[1]
    y = np.zeros((m,))
    for i in range(m):
        for j in range(n):
            y[i] += A[i,j]*x[j]
    return y

# MPI setup
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Initialize matrix and vector
m = 1000
n = 1000
A = np.random.rand(m, n)
x = np.random.rand(n,)

# Scatter the matrix and vector
sendcounts = [m//size]*size
sendcounts[-1] += m % size
senddispls = [sum(sendcounts[:i]) for i in range(size)]
local_A = np.zeros((sendcounts[rank], n), dtype=float)
comm.Scatterv([A, sendcounts, senddispls, MPI.DOUBLE], local_A, root=0)

sendcounts = [n//size]*size
sendcounts[-1] += n % size
senddispls = [sum(sendcounts[:i]) for i in range(size)]
local_x = np.zeros(sendcounts[rank], dtype=float)
comm.Scatterv([x, sendcounts, senddispls, MPI.DOUBLE], local_x, root=0)

# Matrix-vector multiplication on each process
local_y = matrix_vector_mult(local_A, local_x)

# Gather the results
recvcounts = [m//size]*size
recvcounts[-1] += m % size
recvdispls = [sum(recvcounts[:i]) for i in range(size)]
y = np.zeros((m,), dtype=float)
comm.Gatherv(local_y, [y, recvcounts, recvdispls, MPI.DOUBLE], root=0)

# Compute the dot product on the root process
if rank == 0:
    start_time = time.time()
    y_dot = np.dot(A, x)
    dot_time = time.time() - start_time
    
    # Compare the results
    error = np.linalg.norm(y-y_dot)
    print("CPU time of parallel multiplication using {} processes is {:.6f}".format(size, dot_time))
    print("The error comparing to the dot product is :", error)
