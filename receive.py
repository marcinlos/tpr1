
from mpi4py import MPI
from array import array

buf = array('c', '\0') * 1000000 

def ReceiveString():
   comm = MPI.COMM_WORLD
   status = MPI.Status()
   data = comm.Recv(buf, source=0, status=status)
   n = status.Get_count(MPI.CHAR)
   return buf[:n].tostring()
