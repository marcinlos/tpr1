#!/usr/bin/env python

from subprocess import Popen, PIPE
import sys

class AvgCollector(object):
    def __init__(self):
        self.results = dict()
    
    def update(self, key, val):
        if key not in self.results:
            self.results[key] = (0, 0)
        v, n = self.results.get(key)
        self.results[key] = (v + val, n + 1)

    def getResults(self):
        res = dict() 
        for k, (v, n) in self.results.items():
            res[k] = v / n
        return res

prog = sys.argv[1]

count = 5000
runs = 4

sizes = [10, 20, 50, 100, 500, 1000, 1500, 
         2000, 3000, 4000, 5000, 
         6000, 7000, 8000, 9000, 10000,
         15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000,
         55000, 60000, 65000, 70000, 75000, 80000, 85000, 90000, 
         95000, 100000]

def run(kind, size):
    p = Popen('./run {0} {1} {2} {3}'.format(prog, kind, size, count), 
            shell=True, stdout=PIPE)
    output = p.stdout.read()
    return float(output)

def saveResults(res, path):
    out = open(path, 'w')
    for size in sizes:
        time = res[size]
        avg = time / count
        tp = count * size / time
        out.write('{0}\t{1}\t{2}\t{3}\n'.format(size, time, avg, tp))
    out.close()


stdAvg = AvgCollector()
immAvg = AvgCollector()

for _ in xrange(0, runs):
    print('run {0}'.format(_))
    for size in sizes:
        print('size = {0}'.format(size))
        stdAvg.update(size, run('std', size))
        immAvg.update(size, run('sync', size))

saveResults(stdAvg.getResults(), 'std.dat')
saveResults(immAvg.getResults(), 'sync.dat')


