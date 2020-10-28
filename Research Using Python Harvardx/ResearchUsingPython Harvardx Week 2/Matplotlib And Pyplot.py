import matplotlib.pyplot as plt
import numpy as np
print(plt.plot([0,1,4,9,16]))
#plt.show()

x = np.linspace(0,10,20)   #LINEAR VECTOR , STARTING = 0 , ENDING = 10 , 20 POINTS
y1 = x**2.0
y2 = x**1.5
#plt.plot(x,y1,"bo-")   third argument secifies appearance of plot  , blue , circle and straight line
plt.plot(x,y1,"bo-", linewidth = 5, markersize = 8)
plt.plot(x,y2,"gs-", linewidth = 2, markersize = 4)   # green and solid
plt.show()

plt.plot([0,1,2],[0,1,4],"rd-")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,20)   #LINEAR VECTOR , STARTING = 0 , ENDING = 10 , 20 POINTS
y1 = x**2.0
y2 = x**1.5
#plt.plot(x,y1,"bo-")   third argument secifies appearance of plot  , blue , circle and straight line
plt.plot(x,y1,"bo-", linewidth = 5, markersize = 8, label= "Fisrt")
plt.plot(x,y2,"gs-", linewidth = 2, markersize = 4, label = "Second")   # green and solid
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5,10,-5,5])  #(xmin,xmax,ymin,ymax)
plt.legend(loc = "upper right")
plt.show()
plt.savefig("myfirstplot.png")

x = np.linspace(0,10,20)   #LINEAR VECTOR , STARTING = 0 , ENDING = 10 , 20 POINTS
y1 = x**2.0
y2 = x**1.5
#plt.plot(x,y1,"bo-")   third argument secifies appearance of plot  , blue , circle and straight line
plt.loglog(x,y1,"bo-", linewidth = 5, markersize = 8, label= "Fisrt")
plt.loglog(x,y2,"gs-", linewidth = 2, markersize = 4, label = "Second")   # green and solid
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5,10,-5,5])  #(xmin,xmax,ymin,ymax)
plt.legend(loc = "upper right")
plt.show()
plt.savefig("myfirstplot.png")

x = np.linspace(-1,1,20)   #LINEAR VECTOR , STARTING = 0 , ENDING = 10 , 20 POINTS
y1 = x**2.0
y2 = x**1.5
#plt.plot(x,y1,"bo-")   third argument secifies appearance of plot  , blue , circle and straight line
plt.loglog(x,y1,"bo-", linewidth = 5, markersize = 8, label= "Fisrt")
plt.loglog(x,y2,"gs-", linewidth = 2, markersize = 4, label = "Second")   # green and solid
plt.xlabel("X")
plt.ylabel("Y")
plt.axis([-0.5,10,-5,5])  #(xmin,xmax,ymin,ymax)
plt.legend(loc = "upper right")
plt.show()
plt.savefig("myfirstplot.png")


import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(0,1,10)
y = x**2
plt.loglog(x,y,"bo-")
plt.show()

x = np.random.normal(size=1000)
plt.hist(x,bins=np.linspace(-5,5,20))
plt.show()

import matplotlib.pyplot as plt
import numpy as np

y = np.random.gamma(2,3,10000)

plt.figure()
plt.subplot(3,3,3)
plt.hist(y,bins=20)
plt.show()
plt.subplot(222)
plt.hist(y, normed = True, bins = 30)
plt.show()
plt.subplot(223)
plt.hist(y, cumulative = True, bins =  30)
plt.show()
plt.subplot(224)
plt.hist(y, cumulative = True, bins =  30, normed = True, histtype="step")