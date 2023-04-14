"""
#Exercice 4 : Scattering Matrix
1. Create an n by m matrix A on processor 0.
2. Use MPI_Scatterv to send parts of the matrix to the other processors.
3. Processor 1 receives A(i,j) for i=0 to (n/2)-1 and j=m/2 to m-1.
4. Processor 2 receives A(i,j) for i=n/2 to n-1 and j=0 to (m/2)-1.
5. Processor 3 receives A(i,j) for i=n/2 to n-1 and j=m/2 to m-1.

"""

from mpi4py import MPI
import numpy as np

COMM = MPI.COMM_WORLD
SIZE = COMM.Get_size()
RANK = COMM.Get_rank()

n, m = 8, 8 

if RANK == 0:
    matrix = np.random.randint((n,m))
else:
    matrix = None

loc = np.empty((n//2, m//2), dtype=int)
    

COMM.Scatterv(matrix, loc, root=0)

print(f"Process {RANK} received:\n{loc}")
MPI.Finalize()

