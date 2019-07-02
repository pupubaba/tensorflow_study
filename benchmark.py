from itertools import combinations_with_replacement as cwr

benchmark = [
    "is",
    "mg",
    "ep",
    "cg",
    "ft",
    "bt",
    "sp",
    "lu",
    "dt",
]
thead_num = 7
sum = []
total = 0
for i in range(thead_num):
    sum += list(cwr(benchmark,i+1))
    total += len(list(cwr(benchmark,i+1)))
for i in range(1):
    print(total)