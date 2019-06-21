import pickle
import subprocess
import time

result_x = []
result_y = []
x = []
y = []
save_x = []
save_y = []
data_num = 3

for i in range(data_num):
    #Start the benchmark for the event.
    if __name__ == '__main__':
        proc = subprocess.Popen(["sbatch", "event.mpi"],stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:break
            event_out = str(line).split()
    time.sleep(5)

    #Start the benchmark for the power
    if __name__ == '__main__':
        proc = subprocess.Popen(["sbatch", "power.mpi"],stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:break
            power_out = str(line).split()
    file_num = event_out[-1][0:3]
    time.sleep(7)

    #Start indexing for events
    if __name__ == '__main__':
        proc = subprocess.Popen(["cat", "event."+file_num+".out"],stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            event_out = str(line).split()
            result_x.extend(event_out)
    print(result_x)
    
    event = [
        'INST_RETIRED.ANY',
        'CPU_CLK_UNHALTED.THREAD_ANY',
        'UOPS_ISSUED.ANY',
        'RESOURCE_STALLS.ANY',
        'BR_MISP_RETIRED.ALL_BRANCHES',
        'BR_INST_RETIRED.ALL_BRANCHES',
        'FP_ARITH_INST_RETIRED.128B_PACKED_DOUBLE',
        'FP_ARITH_INST_RETIRED.128B_PACKED_SINGLE',
        'FP_ARITH_INST_RETIRED.256B_PACKED_DOUBLE',
        'FP_ARITH_INST_RETIRED.256B_PACKED_SINGLE',
        'FP_ARITH_INST_RETIRED.SCALAR_DOUBLE',
        'FP_ARITH_INST_RETIRED.SCALAR_SINGLE',
        'MEM_LOAD_RETIRED.L1_HIT',
        'L1-dcache-load-misses',
        'LLC-loads',
        'LLC-load-misses',
    ]
    for i in range(len(result_x)):
        for j in range(len(event)):
            if result_x[i] == event[j]:
                x.append(float(result_x[i - 1].replace(",","")))
        if len(x) == len(event):
            save_x.append(x)
            x=[]
        
    print(x)
    file_num = power_out[-1].replace("")


    #Start indexing for power
    if __name__ == '__main__':
        proc = subprocess.Popen(["cat", "power."+file_num+".out"],stdout=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            power_out = str(line).split()
            result_y.extend(power_out)
    print(result_y)

    power = [
        'power/energy-pkg/',
        'power/energy-ram/',
    ]

    tem = 0.0
    b = 0
    for i in range(len(result_y)):
        for j in range(len(power)):
            if result_y[i] == power[j]:
                tem += float(result_y[i - 2])
                b += 1
        if b==2:
            y.append(tem)
            b = 0
            tem = 0
            save_y.append(y)
            y=[]
    result_x = []
    result_y = []

print(save_x)
print(save_y)
with open('data_set.p', 'wd') as file:
    pickle.dump(save_x, file)
    pickle.dump(save_y, file)