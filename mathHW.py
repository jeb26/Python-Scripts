x = 0.0
y = 0.0
z = 0.0

while (((z+3)/3)+((z+5)/8)) != 1.0:
    for i in range(14,1000,1):
        for j in range(-100,1,1):
            if (j == 0):
                continue
            z = (i * 1.0) / j
            print(i,"/",j,"=",z)

print("answer is: ",z)
