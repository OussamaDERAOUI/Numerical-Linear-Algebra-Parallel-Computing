"""
#Exercice 2
Create a program that obtains an integer input from the terminal and distributes it to all the MPI processes. Each process must display its rank and the received value. Keep reading values until a negative integer is entered. Output Example
10
Process 0 got 10
Process 1 got 10
"""

from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()

while True:
    
    if RANK == 0:
        value = int(input('input a value: '))
    else:
        value = None 
    value = COMM.bcast(value,root=0)

    if value <0:
        break

    print('processor {} got {}'.format(RANK,value))
    COMM.Barrier()

MPI.Finalize()
