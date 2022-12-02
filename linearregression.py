#import the models
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import linear_model

house_price =[254,354,645,678]
size=[1400,1600,1700,1100]

size2=np.array(size).reshape((-1,1))

regr=linear_model.LinearRegression()
regr.fit(size2,house_price)

print("COFFICIENT",regrf.coef_)
print("INTERCEPT",rfegr.intercept_)

def graph(formula,x_range):
    x=np.array(x_range)
    y=eval(formula)
    plt.plot(x,y)
    
graph('regr.coef_*x+regr.intercept_',range(1000,2700))
plt.scatter(size,house_price,color='b')
plt.ylabel("HOUSE PRICE")
plt.xlabel("SICE OF HOUSE")
plt.show()