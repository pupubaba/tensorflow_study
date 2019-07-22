import subprocess

test = ["14", "1234", "35662"]
proc = []
j = 0

if __name__ == "__main__":
    for i in test:
        proc.append(subprocess.Popen(["ls"], stdout=subprocess.PIPE))
        j += 1
    for i in range(j+1):
        while True:
            line[i] = proc[i].stdout.readline()
            if not line[i]:break
            print(line[i])