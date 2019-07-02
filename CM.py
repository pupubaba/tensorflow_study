from itertools import combinations_with_replacement as cwr
from multiprocessing import Process
import subprocess
import pickle
import sys

benchmark_list = [
    "bt.B.16", "cg.B.16", "cg.C.16", "dt.C.x", "ep.B.8", "ft.B.16", "ft.C.16", "is.B.8", "lu.B.16", "lu.C.16", "mg.B.8", "sp.B.16",
    "bt.C.16", "cg.B.8", "dt.B.x", "ep.B.16", "ep.C.16", "ft.B.8", "is.B.16", "is.C.16", "lu.B.8",  "mg.B.16", "mg.C.16", "sp.C.16",
]

if __name__ == '__main__':
    if len(sys.argv) is 2:
        print("NODE is NULL")
        sys.exit(1)
    elif len(sys.argv) is 1:
        print("Benchmark is NULL")
        sys.exit(1)
    elif not sys.argv[1] in benchmark_list:
        print("Please chack benchmark name")
        sys.exit(1)

thead_num = sys.argv[1].split(".")[-1]
event_file = """#!/bin/bash

#SBATCH -J test               # Job name
#SBATCH -o test.%j.out         # Name of stdout output file (%j expands to jobId)
##SBATCH -N 1                  # Total number of nodes requested
#SBATCH -n {thead_num}                # Total number of mpi tasks requested
#SBATCH -t 01:30:00           # Run time (hh:mm:ss) - 1.5 hours

# Launch MPI-based executable

perf stat -I 500 -e INST_RETIRED.ANY,CPU_CLK_UNHALTED.THREAD_ANY,UOPS_ISSUED.ANY,RESOURCE_STALLS.ANY,BR_MISP_RETIRED.ALL_BRANCHES,BR_INST_RETIRED.ALL_BRANCHES,FP_ARITH_INST_RETIRED.128B_PACKED_DOUBLE,FP_ARITH_INST_RETIRED.128B_PACKED_SINGLE,FP_ARITH_INST_RETIRED.256B_PACKED_DOUBLE,FP_ARITH_INST_RETIRED.256B_PACKED_SINGLE,FP_ARITH_INST_RETIRED.SCALAR_DOUBLE,FP_ARITH_INST_RETIRED.SCALAR_SINGLE,MEM_LOAD_RETIRED.L1_HIT,L1-dcache-load-misses,LLC-loads,LLC-load-misses prun NPB3.3.1/NPB3.3-MPI/bin/is.B.8 prun NPB3.3.1/NPB3.3-MPI/bin/""".format(thead_num=thead_num)

f = open("test.mpi","w")
f.write(event_file+sys.argv[1])
f.close()

if __name__ == '__main__':
    proc = subprocess.Popen(["sbatch", "-w", "node["+sys.argv[2]+"]", "event.mpi"],stdout=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:break
        event_out = str(line).split()
file_num = event_out[-1].replace(",", "")

if __name__ == '__main__':
    proc = subprocess.Popen(["python", "CMP.py", file_num, sys.argv[1]], stdout=subprocess.PIPE)
    print(proc.stdout.readline())