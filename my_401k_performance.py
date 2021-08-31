# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 09:01:55 2021

@author: john.hanks
"""
import matplotlib.pyplot as plt
import numpy as np

# Input Variables
years_until_retirement = 40
initial_salary = 70_000
employee_contribution_percent = .10
yearly_raise = .06
employer_match_per = .50


############ Questions ##################

# What is your salary in 40 years


# How much money will be in your 401k at the end of 40 years?


# What is the difference in 401k totals with and without employer contribution match?


# In what year do you reach $1M



################# Solutions ##############

# What is your salary in 40 years
s=[]
s.append(initial_salary)

for y in range(1,years_until_retirement+1):
    salary = initial_salary * (1 + yearly_raise)**y
    s.append(salary)



plt.figure(1)
plt.plot(s, label='salary')
plt.title('Salary over Time')
plt.legend(loc='upper left')
plt.xlabel('years')
plt.ylabel('$')

txt = "my salary in {} years is ${}"
print(txt.format(years_until_retirement,round(s[-1]),6))



# How much money will be in your 401k at the end of 40 years?
# What is the difference in 401k totals with and without employer contribution match?
# In what year do you reach $1M
s=[]
yearly_401k=[]
total_401k=[]
yearly_401k_with_employer_match = []
total_401K_with_employer_match = []
s.append(initial_salary)
mill_flag = False
for y in range(1,years_until_retirement+1):
    salary = initial_salary * (1 + yearly_raise)**y
    s.append(salary)
    my_401K = (salary*employee_contribution_percent)* (1 + yearly_raise)
    my_401K_with_employer_match = (salary*employee_contribution_percent + salary*employee_contribution_percent*employer_match_per)* (1 + yearly_raise)
    yearly_401k.append(my_401K)
    total_401k.append(np.sum(yearly_401k))
    yearly_401k_with_employer_match.append(my_401K_with_employer_match)
    total_401K_with_employer_match.append(np.sum(yearly_401k_with_employer_match))
    if (total_401K_with_employer_match[-1] >= 1_000_000) and (mill_flag == False):
        mill_flag = True
        year_of_mill = y

plt.figure(2)
plt.plot(total_401k, label="401K $'s")
plt.title('401K Savings w/o Employer Match')
plt.legend(loc='upper left')
plt.xlabel('years')
plt.ylabel('$')


plt.figure(3)
plt.plot(total_401K_with_employer_match)
plt.title('401K Savings with Employer Match')
plt.legend(loc='upper left')
plt.xlabel('years')
plt.ylabel('$')

diff = total_401K_with_employer_match[-1]-total_401k[-1]
print("Value of employer contribution match = $",np.round(diff,-3))

print("year 410K is > $1M =",year_of_mill)



 
    