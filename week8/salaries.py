import numpy as np

minsalary = 20000
maxsalary = 80000
entries =  10


np.random.seed(1)
salaries = np.random.randint(minsalary, maxsalary, entries)
print(salaries)

salaryplus = salaries + 5000
print(salaryplus)


salarymult = salaries * 1.05
print(salarymult)
newsalaries = salarymult.astype(int)
print(newsalaries)