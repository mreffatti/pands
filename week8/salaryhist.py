import numpy as np
import matplotlib.pyplot as plt

minsalary = 20000
maxsalary = 80000
entries =  10


np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, entries)


plt.hist(salaries)
plt.show()