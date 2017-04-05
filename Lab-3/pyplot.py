#!/usr/bin/env python

import matplotlib.pyplot as plt
import math
import numpy as np

t = np.arange(0.0, np.pi*4.0, 0.01)
s = np.sin(t)

plt.plot(t,s)
plt.title('A sine curve')
plt.xlabel('x')
plt.ylabel('x')
plt.axis([0, np.pi*4, -1 , 1])
plt.show()
