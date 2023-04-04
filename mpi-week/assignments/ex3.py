"""
#Exercice 3
Write a program that takes data from process zero and sends it to all of the other processes by sending it in a ring. That is, process i should receive the data add the rank of the process to it then send it to process i+1, until the last process is reached. Assume that the data consists of a single integer. Process zero reads the data from the user. print the process rank and the value received.

You may want to use these MPI routines in your solution: Send Recv
"""

from mpi4py import MPI

COMM = MPI.COMM_WORLD
RANK = COMM.Get_rank()
SIZE = COMM.Get_size()

if RANK == 0:
    data = int(input('input a value : '))
else:
    data = COMM.recv(source=RANK-1)
    print("Process {} got data {} from process {}".format(RANK,data,RANK-1))

COMM.send(data, dest=(RANK+1)%SIZE)

if RANK == 0:
    data = COMM.recv(source=SIZE-1)
    print("Process {} got data {} from process {}".format(RANK,data,SIZE-1))
MPI.Finalize()