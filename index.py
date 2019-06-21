import subprocess

result=[]
if __name__ == '__main__':
    proc = subprocess.Popen(["ls", "-a"], stdout=subprocess.PIPE ,stderr=subprocess.PIPE)
    while True:
        line = proc.stdout.readline()
        if not line:
            break
        line1 = str(line).split()
        result.extend(line1)
print(result)
y = []
for i in range(len(result)):
    if result[i] == "b'index.py\\n'":
        y.append(result[i])
print(y)