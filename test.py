#!/usr/bin/env python

from mpi4py import MPI
from receive import ReceiveString
from timer import Timer
from time import sleep
import sys

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if len(sys.argv) < 4:
    print 'Usage: ./test.py <std|sync> <message_size> <times>'
    sys.exit(1)

sendType = sys.argv[1]
msgSize = int(sys.argv[2])
repeats = int(sys.argv[3])

t = Timer()

def genMsg(size):
    return ('#TestMessage#', size)

def stdSender():
    msg = genMsg(msgSize)
    for _ in xrange(0, repeats):
        comm.Send(msg, dest=1)

def syncSender():
    msg = genMsg(msgSize)
    for _ in xrange(0, repeats):
        comm.Ssend(msg, dest=1)

def receiver():
    for _ in xrange(0, repeats):
        s = ReceiveString()

functions = { 
    'std': { 0: stdSender, 1: receiver },
    'sync': { 0: syncSender, 1: receiver }
}
            
if rank < 2:
    t.start()
    functions[sendType][rank]()
    t.stop()
    if rank == 0:
        t.printStats(repeats)
else:
    print 'Unexpected rank: {0}'.format(rank)
