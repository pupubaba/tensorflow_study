import subprocess
import time
import sys

if __name__ == "__main__":
    if len(sys.argv) is 1:
        print("file number Error")
        exit(1)
print(sys.argv[1])
file_num = sys.argv[1]
trace_bit = False
pid_list=[]
while True:
    if __name__ == "__main__":
        #proc = subprocess.Popen(['squeue'], stdout=subprocess.PIPE)
        proc = subprocess.Popen(['perf stat -e power/energy-pkg/'], stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:break
            print(line)
            squeue_out = str(line).split()
            if file_num in squeue_out:
                if squeue_out[4] == "R" and trace_bit == False:
                    proc1 = subprocess.Popen(["check pid command"], stdout=subprocess.PIPE)
                    while True:
                        line1 = proc1.stdout.readline()
                        if not line1:break
                        pid_list.extend(str(line1).split("")[1])
                    for i in range(len(pid_list)):
                        proc2 = subprocess.Popen(["perf pid check command"], stdout=subprocess.PIPE)
                    while True:
                        line2 = proc2.stdout.readline()
                        if not line2:break
                        
                     