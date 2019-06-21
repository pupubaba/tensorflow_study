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
]
print(list(cwr(benchmark,12)))