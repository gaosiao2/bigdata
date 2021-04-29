f = open(r"C:\Users\gaosiao\Desktop\test.txt", encoding="utf-8")
lines = f.readlines()
sum=0
n=0
for line in lines:
    sum=float(line.split(",")[16])+sum
    n=n+1
avg=sum/n
print(sum)
print(avg)
