
"""
#Exercice 1
1. Write an MPI program which prints the message "Hello World"

2. Modify your program so that each process prints out both its rank and the total number of processes P that the code is running on, i.e. the size of MPI_COMM_WORLD

3. Modify your program so that only a single controller process (e.g. rank 0) prints out a message (very useful when you run with hundreds of processes).
"""

from mpi4py import MPI 

COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()
SIZE = COMM.Get_size()
if RANK ==0:
    print("hello world", RANK, SIZE)

"""
4. What happens if you omit the final MPI procedure call in your program?

"""