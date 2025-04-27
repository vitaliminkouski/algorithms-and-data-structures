import numpy as np

with open("input.txt", "r") as f:
    n=int(f.readline().strip())
    can_form=np.zeros((n), dtype="int")

    for i in range(n):
        row=np.fromstring(f.readline(), sep=" ", dtype="int")
        for j in range(n):
            if(row[j]==1):
                can_form[j]=i+1

with open("output.txt", "w") as f:
    for i in range(n):
        f.write(f"{can_form[i]} ")
