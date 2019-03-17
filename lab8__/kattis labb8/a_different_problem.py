import sys

for line in sys.stdin:
    etttvå = line.split()
    ett = int(etttvå[0])
    två = int(etttvå[1])
    print(abs(ett - två))