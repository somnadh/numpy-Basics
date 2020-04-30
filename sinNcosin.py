 # trignometic operations using matplotlib and numpy
import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,3*np.pi,0.1)

print("=========================")
n=input("enter which operation do u want\n 1 sin \n 2 cos \n 3 tan")


if n=='1':
    y = np.sin(x)
    plt.plot(x, y)
    plt.show()
elif n=='2':
    y = np.cos(x)
    plt.plot(x, y)
    plt.show()

elif n=='3':
    y = np.tan(x)
    plt.plot(x, y)
    plt.show()

else:
    print("invalid input")