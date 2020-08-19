# -*- coding: utf-8 -*-
import random
random.random()
c=[]
c1=[]
for i in range(0,500):
      c.append(round(random.uniform(10, 500),2))
      c1.append(round(random.uniform(10, 500),2))
for i in range(0,1500):
      c.append(round(random.uniform(500, 1000),2))
      c1.append(round(random.uniform(500, 1000),2))
for i in range(0,20000):
      c.append(round(random.uniform(1000, 4000),2))
      c1.append(round(random.uniform(1000, 4000),2))
for i in range(0,1500):
      c.append(round(random.uniform(4000, 8000),2))
      c1.append(round(random.uniform(1000, 4000),2))
for i in range(0,500):
      c.append(round(random.uniform(8000, 20000),2))
      c1.append(round(random.uniform(8000, 20000),2))
f=open("data3.csv","w")
#f.write("学生支出\n")
#类别1：不经常网购
#类别2：正常网购。
#类别3：喜欢网购
#类别4：花销过大 给警告。
#类别5：网购到了危险的程度。
for i in range(len(c)):
    if c[i]<500:#不经常网购
        f.write(str(c[i]) + ","+"0"+"\n")
    if c[i]>500 and c[i]<1500:#正常网购
        f.write(str(c[i]) + ","+"1"+"\n")
    if c[i]>1500 and c[i]<3000:#喜欢网购
        f.write(str(c[i]) + ","+"2"+"\n")
    if c[i]>3000 and c[i]<5000:#花销大了
        f.write(str(c[i]) + ","+"3"+"\n")
    if c[i]>5000:#危险
        f.write(str(c[i]) + ","+"4"+"\n")
f.close()