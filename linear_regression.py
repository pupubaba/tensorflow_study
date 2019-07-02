import os
import time
from multiprocessing import Process
from multiprocessing import Manager
import sys

prog0 = {# "numactl -C 64,65,16,17 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   #  "taskset -c 26,27,50,51  bodytrack/bodytrack" : "bodytrack/sequenceB_261 4 261 4000 5 0 ${NTHREADS}",\
   # "taskset -c 22,23,30,31 numactl --membind 1 canneal/canneal" : "${NTHREADS} 15000 2000 canneal/2500000.nets 6000",\
   # "taskset -c 0,1,20,21 numactl --membind 1 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\






  ########################
  #  "taskset -c 16,17,62,63  bodytrack/bodytrack" : "bodytrack/sequenceB_261 4 261 4000 5 0 ${NTHREADS}",\
  #  "taskset -c 0,1 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\

  #  "taskset -c 64,65,42,43  bodytrack/bodytrack" : "bodytrack/sequenceB_261 4 261 4000 5 0 ${NTHREADS}",\
  #  "taskset -c 42,43 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
  ########################


   #######################
   # "taskset -c 16,17,62,63 ./facesim":"-timing -threads ${NTHREADS} -lastframe 100",\
   # "taskset -c 50,51,0,1 ferret/ferret/bin/ferret":"ferret/corel lsh ferret/queries 50 20 ${NTHREADS} output.txt",\

   # "taskset -c 14,15,44,45 ./facesim":"-timing -threads ${NTHREADS} -lastframe 100",\
   # "taskset -c 64,65,42,43 ferret/ferret/bin/ferret":"ferret/corel lsh ferret/queries 50 20 ${NTHREADS} output.txt",\
   ######################


   ######################
   # "taskset -c 16,17,62,63 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   # "taskset -c 50,51,0,1 fluidanimate/fluidanimate":"${NTHREADS} 500 fluidanimate/in_500K.fluid out.fluid",\

   # "taskset -c 14,15,44,45 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   # "taskset -c 64,65,42,43 fluidanimate/fluidanimate":"${NTHREADS} 500 fluidanimate/in_500K.fluid out.fluid",\
   ######################


   ####################
   # "taskset -c 0,1 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   # "taskset -c 42,43 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   # "taskset -c 50,51 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   # "taskset -c 44,45 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\



   # "taskset -c 14,15,44,45 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   # "taskset -c 64,65,42,43 fluidanimate/fluidanimate":"${NTHREADS} 500 fluidanimate/in_500K.fluid out.fluid",\
   #####################


   #  "taskset -c 0,1 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   # "taskset -c 0,1 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\



   #  "swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 64,65 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\

###################

   # "taskset -c 16,17 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   # "taskset -c 16,17 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 16,17 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\


   # "taskset -c 22,23 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   # "taskset -c 22,23 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 22,23 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\

###################


   # "taskset -c 50,51 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   # "taskset -c 50,51 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 50,51 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\


   # "taskset -c 14,15 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   # "taskset -c 14,15 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 14,15 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\

##################


   # "taskset -c 62,63 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   # "taskset -c 62,63 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 62,63 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\


   # "taskset -c 6,7 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   # "taskset -c 6,7 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 6,7 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\




   # "taskset -c 0,2,4,6,8,10,12,14 perf stat -e r412E ./swaptions -ns 128 -sm 1000000 -nt 8 ",\



   # "taskset -c 18,19,60,61 ./facesim":"-timing -threads ${NTHREADS} -lastframe 100",\
   # "taskset -c 46,47,182,183 ferret/ferret/bin/ferret":"ferret/corel lsh ferret/queries 50 20 ${NTHREADS} output.txt",\
   # "taskset -c 202,203,186,187 fluidanimate/fluidanimate":"${NTHREADS} 500 fluidanimate/in_500K.fluid out.fluid",\
   # "taskset -c 34,35,56,57 numactl --membind 1 streamcluster/streamcluster":"10 20 128 1000000 200000 5000 none output.txt ${NTHREADS}",\
   # "taskset -c 16,17,84,85,152,153,220,221 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   # "taskset -c 58,59,66,67 vips/vips/bin/vips":"im_benchmark vips/orion_18000x18000.v output.v",\
        }
prog1 = { #"taskset -c 48,49,6,7 blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
    #"taskset -c 14,15,36,37 bodytrack/bodytrack" : "bodytrack/sequenceB_261 4 261 4000 5 0 ${NTHREADS}",\
    #"taskset -c 40,41,32,33 numactl --membind 1 canneal/canneal" : "${NTHREADS} 15000 2000 canneal/2500000.nets 6000",\
    #"taskset -c 62,63,42,43 numactl --membind 1 dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
    #"taskset -c 52,53,2,3 ./facesim":"-timing -threads ${NTHREADS} -lastframe 100",\
    #"taskset -c 44,45,180,181 ferret/ferret/bin/ferret":"ferret/corel lsh ferret/queries 50 20 ${NTHREADS} output.txt",\
    #"taskset -c 82,83,72,73 fluidanimate/fluidanimate":"${NTHREADS} 500 fluidanimate/in_500K.fluid out.fluid",\
    #"taskset -c 8,9,28,29 numactl --membind 1 streamcluster/streamcluster":"10 20 128 1000000 200000 5000 none output.txt ${NTHREADS}",\
    #"taskset -c 54,55,24,25 swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
    #"taskset -c 4,5,12,13 vips/vips/bin/vips":"im_benchmark vips/orion_18000x18000.v output.v",\

   "blackscholes/blackscholes":"${NTHREADS} blackscholes/in_10M.txt prices.txt",\
   "bodytrack/bodytrack" : "bodytrack/sequenceB_261 4 261 4000 5 0 ${NTHREADS}",\
   #"canneal/canneal" : "${NTHREADS} 15000 2000 canneal/2500000.nets 6000",\
   #"dedup/dedup":"-c -p -v -t ${NTHREADS} -i dedup/FC-6-x86_64-disc1.iso -o output.dat.ddp",\
   #"./facesim":"-timing -threads ${NTHREADS} -lastframe 100",\
   #"ferret/ferret/bin/ferret":"ferret/corel lsh ferret/queries 50 20 ${NTHREADS} output.txt",\
   #"fluidanimate/fluidanimate":"${NTHREADS} 500 fluidanimate/in_500K.fluid out.fluid",\
   #"streamcluster/streamcluster":"10 20 128 1000000 200000 5000 none output.txt ${NTHREADS}",\
   #"swaptions/swaptions":"-ns 128 -sm 1000000 -nt ${NTHREADS}",\
   #"vips/vips/bin/vips":"im_benchmark vips/orion_18000x18000.v output.v",\




       }


def benchmark_execution(prog_name,prog_param,num_threads,num):
    start_time = time.time()
    os.system("%s %s >> /dev/null 2>&1" % (prog_name, prog_param))
    
    


if __name__ == '__main__':
    if len(sys.argv) is 1:
        print("parameter is 0")
        sys.exit(1)
    num_threads = sys.argv[1]

    bench_E = [] #Benchmark Execution
    for prog_name,param in prog0.items():
        param = param.replace("${NTHREADS}",num_threads)
        bench_E.append(Process(target=benchmark_execution,args=(prog_name,param,num_threads,0)))

    for prog_name,param in prog1.items():
        param = param.replace("${NTHREADS}",num_threads)
        bench_E.append(Process(target=benchmark_execution,args=(prog_name,param,num_threads,1)))


    for i in range(len(prog0)+len(prog1)):
        bench_E[i].start()
    #    bench_E[i].join()
    for i in range(len(prog0)+len(prog1)):
        bench_E[i].join()

