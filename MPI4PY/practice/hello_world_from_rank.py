from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(f"Hello world...From  {rank}")

# mpiexec -n 4 python hello_world_from_rank.py