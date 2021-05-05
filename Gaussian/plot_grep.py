import re
import matplotlib.pyplot as plt

xlist=[]
ylist=[]

with open('output.txt') as f:
    lines = f.readlines()

regex = re.compile(r"[+-]?(?:\d+\.?\d*|\.\d+)(?:(?:[eE][+-]?\d+)|(?:\*10\^[+-]?\d+))?")

for line in lines:
  data = regex.findall(line)
  ylist.append(float(data[1]))

n = len(ylist) 
for i in range(1,n+1):
  xlist.append(i)

print(xlist)
print(ylist)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.plot(xlist,ylist)
ax.scatter(xlist,ylist)
ax.set_xlabel('step')
ax.set_ylabel('Total Energy (Hartree)')
plt.show()
