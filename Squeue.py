import subprocess
import time
import sys
import re



if __name__ == "__main__":
    if len(sys.argv) is 1:
        print("file number Error")
        exit(1)
    if len(sys.argv) is 2:
        print("benchmark name Error")
        exit(1)
NL=[]
if "," in sys.argv[3]:
    NL=re.findall("\d+", sys.argv[3])
elif "-" in sys.argv[3]:
    tem=re.findall("\d+", sys.argv[3])
    for i in range(int(tem[0]),int(tem[1])+1):
        NL.extend(str(i))
else:
    NL = sys.argv[3]

file_num = sys.argv[1]
trace_bit = False
squeue_out = []
pid_list = []
event = "INST_RETIRED.ANY,CPU_CLK_UNHALTED.THREAD_ANY,UOPS_ISSUED.ANY,RESOURCE_STALLS.ANY,BR_MISP_RETIRED.ALL_BRANCHES,BR_INST_RETIRED.ALL_BRANCHES,FP_ARITH_INST_RETIRED.128B_PACKED_DOUBLE,FP_ARITH_INST_RETIRED.128B_PACKED_SINGLE,FP_ARITH_INST_RETIRED.256B_PACKED_DOUBLE,FP_ARITH_INST_RETIRED.256B_PACKED_SINGLE,FP_ARITH_INST_RETIRED.SCALAR_DOUBLE,FP_ARITH_INST_RETIRED.SCALAR_SINGLE,MEM_LOAD_RETIRED.L1_HIT,L1-dcache-load-misses,LLC-loads,LLC-load-misses "
event_list = []
power_list = []
event_out = []
power = 0.0
LL = []
op=1
mod = sys.modules[__name__]
# while True:
if __name__ == "__main__":
    # proc = subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
    while True:
        proc = subprocess.Popen(["pdsh", "-w", "node["+sys.argv[3]+"]", "pgrep", sys.argv[2]], stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:break
            LL.append(str(line).split())
        if not LL:
            LL = []
        else:break
    for i in LL:
        k=int(re.findall("\d+",i[0])[0])
        globals()['nnl_{}'.format(k)]=""
    for i in LL:
        k=int(re.findall("\d+",i[0])[0])

        #nnl_2+=str(i[1])
        #k=int(re.findall("\d+",i[0])[0])
        #'nnl_{}'.format(k)+=str(i[1])
        jec='nnl_{}'.format(k)
        #a=str(i[1])
        #b='nnl_'+str(k)
        #print(type(a))
        exec("%s = %s + '%s,'" %(jec,jec,str(i[1])))


# squeue_out.extend(str(line).split())
    #if file_num in squeue_out:
    #    if "R" in squeue_out and trace_bit == False:
     #       proc1 = subprocess.Popen(["pdsh", "-w", "node["+sys.argv[3]+"]", "pgrep", sys.argv[2]], stdout=subprocess.PIPE)
      #      while True:
       #         line1 = proc1.stdout.readline()
        #        if not line1:break
         #       pid_list.extend(str(line1).split("")[1])
          #           for i in pid_list:

    print(NL)
    for i in NL:
        exec("kec = %s[:-1]"%'nnl_{}'.format(i))
        print(kec)
        exec("%s = subprocess.Popen(['pdsh', '-w', 'node['+i+']', 'perf', 'stat', '-e', 'instructions', '-p',kec, 'sleep', '3'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)"%'proc{}'.format(i))
        #proc{} = subprocess.Popen(["pdsh", "-w", "node["+i+"]", "perf", "stat", "-e", "instructions", "-p",kec, "sleep", "3"], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #proc2 = subprocess.Popen(["pdsh", "-w", "node["+sys.argv[3]+"]", "pgrep", sys.argv[2]], stdout=subprocess.PIPE)
    for i in NL:
        while True:
            exec("%s = %s.stderr.readline()"%('line{}'.format(i),'proc{}'.format(i)))
            #line2 = proc2.stderr.readline()
            print("a")
            #exec("if not %s:\n    break"%'line{}'.format(i))
            ex = "not line{}".format(i)
            if eval(ex):break
            print("b")
            #if not line2:break
            exec("print(%s)"%'line{}'.format(i))
            #print(line2)
          #trace_bit = True
            # else:break