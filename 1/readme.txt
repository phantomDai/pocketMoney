1，学习率动态变化：初始学习率 / (1+t/(T/2))
   邻域半径动态变化：sigma(t) = sigma / (1 + t/T)，
   其中，t为当前的迭代次数，T为总的迭代次数。
参考：1，https://github.com/JustGlowing/minisom/blob/master/examples/examples.ipynb
      2，https://blog.csdn.net/jyh_AI/article/details/82024431